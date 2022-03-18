/*
 * Small binary to power on/off phonesim modem
 * Copyright (c) 2022  Jolla Ltd.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; version 2 of the License.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 */

#include <QCoreApplication>
#include <QDBusConnection>
#include <QDBusMessage>
#include <QDBusPendingCallWatcher>
#include <QDBusPendingReply>
#include <QDBusVariant>
#include <QDebug>
#include <QThread>

QDBusMessage createPropertyCall(const QString &property, const QVariant &value)
{
    auto call = QDBusMessage::createMethodCall("org.ofono", "/phonesim", "org.ofono.Modem", "SetProperty");
    call << property;
    call << QVariant::fromValue(QDBusVariant(value));
    return call;
}

void setPower(QCoreApplication &app, bool turnOn)
{
    auto message = QDBusConnection::systemBus().asyncCall(createPropertyCall("Powered", turnOn));
    auto *watcher = new QDBusPendingCallWatcher(message, &app);
    QObject::connect(watcher, &QDBusPendingCallWatcher::finished, [&](QDBusPendingCallWatcher *call) {
        bool quit = false;
        QDBusPendingReply<void> reply = *call;
        if (reply.isError()) {
            qWarning() << "Could not power" << (turnOn ? "on" : "off") << "modem:" << reply.error();
            quit = true;
        } else {
            auto message = QDBusConnection::systemBus().asyncCall(createPropertyCall("Online", turnOn));
            auto *watcher = new QDBusPendingCallWatcher(message, &app);
            QObject::connect(watcher, &QDBusPendingCallWatcher::finished, [&](QDBusPendingCallWatcher *call) {
                int status = 0;
                QDBusPendingReply<void> reply = *call;
                if (reply.isError()) {
                    qWarning() << "Could not" << (turnOn ? "online" : "offline") << "modem:" << reply.error();
                    status = 1;
                }
                call->deleteLater();
                app.exit(status);
            });
        }
        call->deleteLater();
        if (quit)
            app.exit(1);
    });
}

int main(int argc, char **argv)
{
    QCoreApplication app(argc, argv);
    if (argc != 2) {
        qWarning() << "Takes one mandatory argument: 'on' or 'off'";
        return 2;
    }
    bool turnOn = false;
    if (strcmp(argv[1], "on") == 0) {
        turnOn = true;
    } else if (strcmp(argv[1], "off") != 0) {
        qWarning() << "The argument must be 'on' or 'off'";
        return 2;
    }
    if (turnOn)
        QThread::sleep(2);
    setPower(app, turnOn);
    return app.exec();
}
