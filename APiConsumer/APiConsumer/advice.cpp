#include "advice.h"
#include <QJsonDocument>

Advice::Advice(QObject *parent) : QObject(parent){

}

void Advice::setAdvice(QString cep )
{

    // create custom temporary event loop on stack
    QEventLoop eventLoop;

    // "quit()" the event-loop, when the network request "finished()"
    QNetworkAccessManager mgr;
    QObject::connect(&mgr, &QNetworkAccessManager::finished, &eventLoop, &QEventLoop::quit);

    // the HTTP request
    QNetworkRequest req(QUrl( QString("http://viacep.com.br/ws/"+cep+"/json/")));
    QNetworkReply *reply = mgr.get(req);
    eventLoop.exec(); // blocks stack until "finished()" has been called

    if (reply->error() == QNetworkReply::NoError) {
        //success
        QString advice = reply->readAll();
        delete reply;
        this->data = advice;
        emit  dataChanged();
        //return advice;
    }
    else {
        //failure
        //QString error = reply->errorString();
        delete reply;
        this->data = "";
        emit  dataChanged();

    }
}

QString Advice::getAdvice()
{
    return this->data;
}

void registerType() {
    qmlRegisterType<Advice>("Models", 1, 0, "Advice");
}
Q_COREAPP_STARTUP_FUNCTION(registerType)
