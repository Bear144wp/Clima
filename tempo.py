import requests

API_KEY = '6bde49323f4aedd4ad642e57aa76a2e5'

while True:
    try:
        cidade = input('Digite a cidade: ')


        link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'

        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp'] - 273
        sensacao_terminca = requisicao_dic['main']['feels_like'] - 273

        print(f'Condição: {descricao}, Temperatura: {temperatura:.0f}ºC, Sensação Térmica: {sensacao_terminca:.0f}ºC')
        break

    except:
        print('Cidade não encontrada, tente novamente!')