#ifndef ADVICE_H
#define ADVICE_H

#include <QObject>
#include <QCoreApplication>
#include <QDebug>
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QUrl>
#include <QUrlQuery>
#include <QQmlEngine>
class Advice : public QObject
{
    Q_OBJECT
    Q_PROPERTY(QString advice READ getAdvice WRITE setAdvice NOTIFY dataChanged)
public:
    explicit Advice(QObject *parent = nullptr);

    Q_INVOKABLE QString getAdvice();
private:
    QString data;
    void setAdvice(QString a);

signals:
    void dataChanged();
};

#endif // ADVICE_H
