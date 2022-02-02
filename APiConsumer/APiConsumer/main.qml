import QtQuick 2.15
import QtQuick.Controls 2.15
import com.advice 1.0
import QtQuick.Layouts 1.15

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Consulta CEP")

    Rectangle {
        anchors.fill: parent
        color: "#99B782"
        Advice{
            id: advice
        }
        Connections {
            target: advice
            function onDataChanged() {
                if(!advice.advice){
                    error.visible = true
                    data.visible = !true
                    return
                }
                let js = JSON.parse(advice.advice)
                cep0.text = "CEP: "+ js.cep
                log.text = js.logradouro
                uf.text = "Estado :" + js.uf
                cidade.text = "Cidade :"+js.localidade
                bairro.text = "Bairro :"+js.bairro
                data.visible = true

                error.visible = !true
            }
        }
        ColumnLayout {
            id: s
            anchors.top: parent.top
            anchors.horizontalCenter: parent.horizontalCenter
            TextField{
                id: cep
                height: 50
                width: 200
                placeholderText: "Digite o cep"
            }
            Rectangle{
                Layout.alignment: Qt.AlignVCenter
                height: 50
                width: 200
                color: "red"
                Button{
                    anchors.fill: parent
                    text: "Pesquisar"
                    onClicked: {
                        error.visible = !true
                        advice.advice = cep.text
                    }
                }
            }
        }
        TextField {
            id:error
            visible: false
            text: "CEP INVALIDO"
            readOnly: true
        }
        ColumnLayout{
            id: data
            visible: false

            anchors.verticalCenter: parent.verticalCenter
            spacing: 0
            TextField {
                id:cep0
                readOnly: true
            }
            TextField {
                id:log
                readOnly: true
            }
            TextField {
                id:uf
                readOnly: true
            }
            TextField {
                id:cidade
                readOnly: true
            }
            TextField {
                id: bairro
                readOnly: true
            }
        }
    }
}
