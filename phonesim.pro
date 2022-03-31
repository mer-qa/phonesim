TARGET = phonesim
TEMPLATE = app
INCLUDEPATH = src
VERSION = 1.20
DEFINES += VERSION=\\\"$$VERSION\\\"

QT = core gui xml network widgets

target.path = /usr/bin
INSTALLS += target

xml.files = src/default.xml src/GSMSpecification.xml
xml.path = /usr/share/phonesim
INSTALLS += xml

HEADERS = \
    src/control.h \
    src/attranslator.h \
    src/gsmspec.h \
    src/gsmitem.h \
    src/phonesim.h \
    src/server.h \
    src/hardwaremanipulator.h \
    src/qsmsmessagelist.h \
    src/qsmsmessage_p.h \
    src/qsmsmessage.h \
    src/qcbsmessage.h \
    src/callmanager.h \
    src/simfilesystem.h \
    src/simapplication.h \
    src/qatresult.h \
    src/qwsppdu.h \
    src/qsimcommand.h \
    src/qsimenvelope.h \
    src/qsimterminalresponse.h \
    src/qsimcontrolevent.h \
    src/qgsmcodec.h \
    src/qatutils.h \
    src/qatresultparser.h

SOURCES = \
    src/main.cpp \
    src/control.cpp \
    src/attranslator.cpp \
    src/gsmspec.cpp \
    src/gsmitem.cpp \
    src/phonesim.cpp \
    src/server.cpp \
    src/hardwaremanipulator.cpp \
    src/qsmsmessagelist.cpp \
    src/qsmsmessage.cpp \
    src/qcbsmessage.cpp \
    src/callmanager.cpp \
    src/simfilesystem.cpp \
    src/simapplication.cpp \
    src/qgsmcodec.cpp \
    src/qatutils.cpp \
    src/qatresultparser.cpp \
    src/qatresult.cpp \
    src/qwsppdu.cpp \
    src/qsimcommand.cpp \
    src/qsimenvelope.cpp \
    src/qsimterminalresponse.cpp \
    src/qsimcontrolevent.cpp \
    src/conformancesimapplication.cpp

FORMS = \
    src/controlbase.ui
