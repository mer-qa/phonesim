TARGET = phonesim
TEMPLATE = app
VERSION = 1.20
DEFINES += VERSION=\\\"$$VERSION\\\"

QT = core gui xml network script dbus widgets

target.path = /usr/bin
INSTALLS += target

xml.files = default.xml
xml.path = /usr/share/phonesim/default.xml
INSTALLS += xml

HEADERS = \
    control.h \
    attranslator.h \
    gsmspec.h \
    gsmitem.h \
    phonesim.h \
    server.h \
    hardwaremanipulator.h \
    qsmsmessagelist.h \
    qsmsmessage_p.h \
    qsmsmessage.h \
    qcbsmessage.h \
    callmanager.h \
    simfilesystem.h \
    simapplication.h \
    qatresult.h \
    qwsppdu.h \
    qsimcommand.h \
    qsimenvelope.h \
    qsimterminalresponse.h \
    qsimcontrolevent.h \
    qgsmcodec.h \
    qatutils.h \
    qatresultparser.h

SOURCES = \
    main.cpp \
    control.cpp \
    attranslator.cpp \
    gsmspec.cpp \
    gsmitem.cpp \
    phonesim.cpp \
    server.cpp \
    hardwaremanipulator.cpp \
    qsmsmessagelist.cpp \
    qsmsmessage.cpp \
    qcbsmessage.cpp \
    callmanager.cpp \
    simfilesystem.cpp \
    simapplication.cpp \
    qgsmcodec.cpp \
    qatutils.cpp \
    qatresultparser.cpp \
    qatresult.cpp \
    qwsppdu.cpp \
    qsimcommand.cpp \
    qsimenvelope.cpp \
    qsimterminalresponse.cpp \
    qsimcontrolevent.cpp \
    conformancesimapplication.cpp

FORMS = \
    controlbase.ui
