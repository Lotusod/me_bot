from iqoptionapi.stable_api import IQ_Option
from datetime import datetime, timedelta
from colorama import init, Fore, Back
from time import time
import pandas as pd
import numpy as np
import gspread
import pwinput
import sys, os, configparser, requests, json, re


init(autoreset=True)


def Conexao():
	global API
	credentials = {

		"type": "service_account",
		"project_id": "license-346910",
		"private_key_id": "dd232c8b3c40c9266259ff5681144be175783961",
		"private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC1oK6c3/SkBWfj\ngq2F2Ex/rwAh1dyo9OXHLTlX+6Zd4Ne14K8pzp2gxj2PNDC1Z4s88c4OVLzqnvX5\nkH3rpaNoFdphlYsDgW2xElbJ8KYKnqRSA4mDLq+0ihNSCfFgLrX7P7zQSdJFj70d\nQnGXDC4K196/luBinKWPYb1pvFPrNVOxscSKp8Giz2ElgJfgNJkpVo6vZDShhWGS\nK1+RD6VTnn8Zh4LIBW9/QSK3CRgv/VrdlLmpZsRR5IbUonPJBw/DY3muE8yYuY0+\noDm+4420NXqEcUJ2hlXZVkYIBZDsr36QwrDNvD/DPzL40ELwYz+/UDo1k5sapWiY\nbZqFPAybAgMBAAECggEAPjkSGQRQl3CSqsq2D8iOTJ/zd6QAuJFNtvKzVoUL9dV1\nkQWsfLIgJlhD9q92kG8ssHBWm2pEXkyfECSEPxq75Ii4C/5jZYwNvEAAI6ah+7ll\nqgM0NRDleQBkphJp8v2NssmfMexYcSRRMZj1uT2e+HAEC7bwoFfyEDD35yVxyn4g\njpA2ZQZ5PbLPj8DkUIxJU/kpTiEYsj9UcUwEohOF72VmJM7FfGGr0wp2CtJuzEle\nAe/K9TqQWvx3VqjwGsuvXq4UwybI2pnX4MS5QHhk26idZ5trwI0XAOmkti3KXSNh\ny+P1swW/ym0CUGQsvpNmlcRveSvM/empTo9QkUJo4QKBgQD/nX1pZntxLmH7DFUO\nBIVVBPO67OL1I+CIH4Mxkx+ynsLmCM54wPR23u9lPsumi3JPR5zapCKAZqPeRkZ7\n/GSwt5Yz9ju0lbYLWds3AF6sxoZReoopl7z6yifhkX79YcyoIs3SY5FWoP8grCNf\nGfAwNdp0ZzOaMQexsSC0dpXPrwKBgQC15q21hebrBQ0POw1Mop8lIB23QzrjO4Lu\ngwZuI5up4dXVbPpqXLp+zE4rmXABUub3NPBKO/q5+0BzEUCSRy+7jwAtfGvpHEut\nX9BvdgdNtDNpnh7iL6QB6upH0qv4E19E/hrMACJlO3Ztox7aOoM9CnOpGaMdTpvD\nH8GqiB3A1QKBgQCUJFQwp8JXAAitFKKesyQK+AnBhdSrOhXBDnJcYuX2AWj3JJd1\nCG8mDWI1DUW9ygd/xwMy+/k67UF/ar8i0E4S1PNqPgSwTivpPDR+FerIu23Q/vHf\n1R8jQdIHOumcM/gGYdVjX202BayW5OzDCydW6X8oAz+21z+cTgmkTS3Z5QKBgQCi\nKJsDD/Pj4ATcZxBcGT02o4LaNRzyJcN7TWMWHLhQofs24If8+d1n3Epzo72t8HHm\nP1NXWlESK2IxMlgWD1AGLF1EL38juQ3d6WSveNDZ/KM4rLVrfnz/GKTykmSsKtjr\ncHwDELuY84GIC7sdYLxOVlr1jN1U6xcAw/aqR93+YQKBgBB4iVysQwv9R6j1fwaY\nqwKSLu/zzepNObxsG9NEfZv7cQyv7SNNPVT1Ufef6Fw1qfLy5kwmDRXR9hsdDNwi\nLf4vx2AiOqSMU5SuGebqmt6iPVyk4sh2ruOP0nSF4w1giNlFwRiRi1BjOk72QVev\ntNa2mi7PqTGkjYeWsy0QfZtG\n-----END PRIVATE KEY-----\n",
		"client_email": "license-service@license-346910.iam.gserviceaccount.com",
		"client_id": "113638494652301183827",
		"auth_uri": "https://accounts.google.com/o/oauth2/auth",
		"token_uri": "https://oauth2.googleapis.com/token",
		"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
		"client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/license-service%40license-346910.iam.gserviceaccount.com"
	}

	gc = gspread.service_account_from_dict(credentials)
	sh = gc.open_by_key("1nMy_aiR1KpZnuEbSvDyasLeriVup5szkvIZHJwmP7xU")
	worksheet = sh.sheet1
	col = worksheet.col_values(1)

	arquivo = configparser.RawConfigParser()
	arquivo.read('config.txt')

	if arquivo.read('config.txt'):
		emailsd = arquivo.get('USER_CONFIG', 'email')


	else:
		email = input('\n Email   :: ')
		password = input('\n Password:: ')
		Percentage = input('\n\n How many Percentage of trand do you want:: ')
		Martingale = input('\n\n How many Martingale do you want:: ')

		myfile = open('config.txt', 'w')
		
		myfile.write('[USER_CONFIG]' + '\n')
		myfile.write('Email = ' + email + '\n')
		myfile.write('Password = ' + password + '\n')
		myfile.write('porcentagem = ' + Percentage + '\n')
		myfile.write('martingale = ' + Martingale + '\n')
		sys.exit()

	print('\n Email   :: ', end='')
	email = input()

	password = pwinput.pwinput('\n Password:: ', mask="●")

	API = IQ_Option(email, password)

	if emailsd in col:
		print(Fore.LIGHTYELLOW_EX +'\n █▓▓▒▒░░ Verified license! ░░▒▒▓▓█ '+ Fore.RESET)
	else:
		print(Fore.RED +'\n █▓▓▒▒░░ Unverified license ░░▒▒▓▓█'+ Fore.RESET, Fore.YELLOW +'\n Contact support to obtain the license!!'+ Fore.RESET)
		input('\n  press enter to exit \n')
		sys.exit()

	API.connect()

	if API.check_connect():
		print(Fore.LIGHTGREEN_EX + '\n       connection succeeded!' + Fore.RESET)
	else:
		
		print(Fore.RED +'\n  Error connecting'+ Fore.RESET,Fore.LIGHTCYAN_EX +''' ..The account has no match with IQ OPTION platform'''+ Fore.RESET)
		input(Fore.YELLOW +'\n  Press enter to exit'+ Fore.RESET)
		sys.exit()

def Configuracoes():
	global config
	config = {}
	arquivo = configparser.RawConfigParser()
	arquivo.read('config.txt')

	# Transforma a string timeframe em uma lista de inteiros com os timeframes
	config['timeframe'] = list(map(int, input('\n\n  Which timeframe do you want to Analysis :: ').split(',')))
	config['dias'] = input('\n  How many days do you want to review :: ')
	config['porcentagem'] = arquivo.get('USER_CONFIG', 'porcentagem')
	config['martingale'] = arquivo.get('USER_CONFIG', 'martingale')
	config['todos_pares'] = 'N'
	config['arquivo_saida'] = 'Signal_list_checker.txt'
	config['check_lista'] = 'N'
	config['validar_sinal'] = input('\n  Do you want at that time the parity is open :: ')
	if config['validar_sinal'] == '':
		print(Fore.RED + '                                        Disable'+ Fore.RESET)
	config['tendencia'] = input('\n  Do you want to follow trend :: ')
	if config['tendencia'] == 'Y':
		config['tendencia_porcentagem'] = int(input('\n  How many Percentage of trend do you want :: '))
	if config['tendencia'] == 'y':
		config['tendencia_porcentagem'] = int(input('\n  How many Percentage of trend do you want :: '))
	else:
		print(Fore.RED + '                        Disable'+ Fore.RESET)


def Clear_Screen():
	sistema = os.name
	if sistema == 'nt':
		os.system('cls')
	else:
		os.system('clear')


def cataloga(par, dias, prct_call, prct_put, timeframe, data_atual):
	data = []
	datas_testadas = []
	time_ = time()
	sair = False
	while sair == False:
		velas = API.get_candles(par, (timeframe * 60), 1000, time_)
		velas.reverse()
		posicao = 0
		for x in velas:

			if datetime.fromtimestamp(x['from']).strftime('%Y-%m-%d') != data_atual:
				if datetime.fromtimestamp(x['from']).strftime('%Y-%m-%d') not in datas_testadas:
					datas_testadas.append(datetime.fromtimestamp(x['from']).strftime('%Y-%m-%d'))

				if len(datas_testadas) <= dias:
					x.update({'cor': 'verde' if x['open'] < x['close'] else 'vermelha' if x['open'] > x['close'] else 'doji'})
					if config['tendencia'] == 'Y':
						velas_tendencia = velas[posicao:posicao + periodo_ema]
						tendencia = Verificar_Tendencia(velas_tendencia)
						x.update({'tendencia': tendencia})
						data.append(x)
					if config['tendencia'] == 'y':
						velas_tendencia = velas[posicao:posicao + periodo_ema]
						tendencia = Verificar_Tendencia(velas_tendencia)
						x.update({'tendencia': tendencia})
						data.append(x)
					else:
						data.append(x)
				else:
					sair = True
					break
			posicao += 1

		time_ = int(velas[-1]['from'] - 1)

	analise = {}
	for velas in data:
		horario = datetime.fromtimestamp(velas['from']).strftime('%H:%M')
		if horario not in analise:
			analise.update({horario: {'verde': 0, 'vermelha': 0, 'doji': 0, '%': 0, 'dir': '', 'tendencia': 0, 'contra_verde': 0, 'contra_vermelha': 0}})
		analise[horario][velas['cor']] += 1
		if config['tendencia'] == 'Y':
			if velas['cor'] != velas['tendencia']:
				if velas['cor'] == 'verde':
					analise[horario]['contra_verde'] += 1
				else:
					analise[horario]['contra_vermelha'] += 1
		if config['tendencia'] == 'y':
			if velas['cor'] != velas['tendencia']:
				if velas['cor'] == 'verde':
					analise[horario]['contra_verde'] += 1
				else:
					analise[horario]['contra_vermelha'] += 1

		try:
			analise[horario]['%'] = round(100 * (analise[horario]['verde'] / (analise[horario]['verde'] + analise[horario]['vermelha'] + analise[horario]['doji'])))
		except:
			pass

	for horario in analise:
		if analise[horario]['%'] > 50: analise[horario]['dir'] = 'CALL'
		if analise[horario]['%'] < 50: analise[horario]['%'], analise[horario]['dir'] = 100 - analise[horario]['%'], 'PUT '
		if config['tendencia'] == 'Y':
			if analise[horario]['dir'] == 'CALL':
				analise[horario]['tendencia'] = int(100 - ((analise[horario]['contra_verde'] / analise[horario]['verde']) * 100))
			else:
				analise[horario]['tendencia'] = int(100 - ((analise[horario]['contra_vermelha'] / analise[horario]['vermelha']) * 100))
		if config['tendencia'] == 'y':
			if analise[horario]['dir'] == 'CALL':
				analise[horario]['tendencia'] = int(100 - ((analise[horario]['contra_verde'] / analise[horario]['verde']) * 100))
			else:
				analise[horario]['tendencia'] = int(100 - ((analise[horario]['contra_vermelha'] / analise[horario]['vermelha']) * 100))

	return analise


def Verificar_Tendencia(velas_tendencia):
	fechamento = round(velas_tendencia[0]['close'], 4)
	df = pd.DataFrame(velas_tendencia)
	EMA = df['close'].ewm(span=periodo_ema, adjust=False).mean()
	for data in EMA:
		EMA_line = data

	if EMA_line > fechamento:
		dir = 'vermelha'
	elif fechamento > EMA_line:
		dir = 'verde'
	else:
		dir = False

	return dir


def Obter_Paridades():
	P = API.get_all_open_time()
	paridades = []
	if config['todos_pares'] == 'S':
		for pares in P['digital']:
			paridades.append(pares)
		for pares in P['turbo']:
			paridades.append(pares)
	else:
		for pares in P['digital']:
			if P['digital'][pares]['open'] == True:
				paridades.append(pares)
		for pares in P['turbo']:
			if P['turbo'][pares]['open'] == True:
				paridades.append(pares)

	return np.unique(paridades)


def Obter_Horario_Paridades():
	info_binarias = {}
	info_digitais = {}
	url = 'https://fininfo.iqoption.com/api/graphql'
	arquivo_payload = open('payload_post.txt', 'r')
	requisicao = requests.post(url, data=arquivo_payload)
	dados = json.loads(requisicao.text)
	for data in dados['data']['BinaryOption']:
		if data['type'] == 'Forex' and len(data['schedule']) != 0:
			x = []
			y = {}
			paridade = data['name']
			y['data'] = data['schedule'][0]['from'].split('T')[0]
			y['abertura'] = data['schedule'][0]['from'].split('T')[1].split('-')[0]
			y['fechamento'] = data['schedule'][0]['to'].split('T')[1].split('-')[0]
			x = [y]
			paridade = String_Format(paridade)
			info_binarias[paridade] = x

	for data in dados['data']['DigitalOption']:
		if data['type'] == 'Forex' and len(data['schedule']) != 0:
			x = []
			y = {}
			paridade = data['name']
			y['data'] = data['schedule'][0]['from'].split('T')[0]
			y['abertura'] = data['schedule'][0]['from'].split('T')[1].split('-')[0]
			y['fechamento'] = data['schedule'][0]['to'].split('T')[1].split('-')[0]
			x = [y]
			paridade = String_Format(paridade)
			info_digitais[paridade] = x

	return info_binarias, info_digitais


def String_Format(string_par):
	format_string = string_par.replace('/', '')
	if re.match("[A-Z]{6} .{5}", format_string):
		format_string = format_string.split(' ')
		format_string = format_string[0] + '-OTC'

	return format_string


def Valida_Sinal(info_binarias, info_digitais, horario, paridade, data_atual):
	if paridade in info_binarias:
		if data_atual == info_binarias[paridade][0]['data']:
			abertura = info_binarias[paridade][0]['abertura']
			fechamento = info_binarias[paridade][0]['fechamento']
			# dif_abertura: Retorna um numero positivo caso o horario do sinal seja maior que o horario de abertura da paridade. Ex: Horario do sinal 01:15 e abertura da paridade é de 01:00, irá retornar 15, que é a diferença em minutos.
			dif_abertura = int((datetime.strptime(horario, '%H:%M') - datetime.strptime(abertura, '%H:%M:%S')).total_seconds() / 60)
			# dif_fechamento: O inverso de dif_abertura. retorna um numero negativo (que é a diferença em minutos) se o horario do sinal for menor que o horario de fechamento da paridade.
			dif_fechamento = int((datetime.strptime(horario, '%H:%M') - datetime.strptime(fechamento, '%H:%M:%S')).total_seconds() / 60)
			# Verifica se o sinal esta dentro do horario de funcionamento da paridade, e retorna True caso esteja.
			if dif_abertura > 0 and dif_fechamento < 0:
				return True

	if paridade in info_digitais:
		if data_atual == info_digitais[paridade][0]['data']:
			abertura = info_digitais[paridade][0]['abertura']
			fechamento = info_digitais[paridade][0]['fechamento']
			# dif_abertura: Retorna um numero positivo caso o horario do sinal seja maior que o horario de abertura da paridade. Ex: Horario do sinal 01:15 e abertura da paridade é de 01:00, irá retornar 15, que é a diferença em minutos.
			dif_abertura = int((datetime.strptime(horario, '%H:%M') - datetime.strptime(abertura, '%H:%M:%S')).total_seconds() / 60)
			# dif_fechamento: O inverso de dif_abertura. retorna um numero negativo (que é a diferença em minutos) se o horario do sinal for menor que o horario de fechamento da paridade.
			dif_fechamento = int((datetime.strptime(horario, '%H:%M') - datetime.strptime(fechamento, '%H:%M:%S')).total_seconds() / 60)
			# Verifica se o sinal esta dentro do horario de funcionamento da paridade, e retorna True caso esteja.
			if dif_abertura > 0 and dif_fechamento < 0:
				return True
	# Retorna False caso não satisfaça nenhuma condição
	return False


def Escreve_Arquivo(arquivo_saida, timeframe, par, horario, direcao, data_atual, martingale):
	open(arquivo_saida, 'a').write('M' + str(timeframe) + ',' + par + ',' + horario + ',' + direcao + '\n')
	open('Signal_list.txt', 'a').write(horario + ',' + par + ',' + direcao + '\n')
	if check_lista == 'S':
		open(str(arquivo_saida) + '-CHECK', 'a').write(f'{data_atual} {str(horario) + ":00"} {par} {direcao} {str(martingale) + "GL"} {str(timeframe) + "TM"}\n')


Clear_Screen()
print('=========================================\n|         CATALOGADOR DE SINAIS         |\n=========================================')


try:
	Conexao()
	Configuracoes()
	

	arquivo_saida = config['arquivo_saida']
	check_lista = config['check_lista']
	timeframe_config = config['timeframe']
	dias = int(config['dias'])
	porcentagem = int(config['porcentagem'])
	martingale = config['martingale']
	prct_call = abs(porcentagem)
	prct_put = abs(100 - porcentagem)
	periodo_ema = 20
	paridades = Obter_Paridades()
	data_atual = datetime.now().strftime('%Y-%m-%d')
	info_binarias, info_digitais = Obter_Horario_Paridades()
	print(f'\n\n{Fore.GREEN}>>>>>CATALOGING {len(paridades)} PAIR IN {len(timeframe_config)} TIMEFRAME(S)<<<<<\n')
	for timeframe in timeframe_config:
		catalogacao = {}
		contador = 1
		for par in paridades:
			timer = int(time())
			print(f'{contador} - {Fore.GREEN}CATALOGING - {Fore.RESET} {Fore.BLUE}{par}{Fore.RESET} | TIMEFRAME {Fore.GREEN}M{timeframe}{Fore.RESET}...', end='')
			catalogacao.update({par: cataloga(par, dias, prct_call, prct_put, timeframe, data_atual)})

			for par in catalogacao:
				for horario in sorted(catalogacao[par]):
					if martingale.strip() != '':

						mg_time = horario
						soma = {'verde': catalogacao[par][horario]['verde'], 'vermelha': catalogacao[par][horario]['vermelha'], 'doji': catalogacao[par][horario]['doji']}

						for i in range(int(martingale)):

							catalogacao[par][horario].update({'mg' + str(i + 1): {'verde': 0, 'vermelha': 0, 'doji': 0, '%': 0}})

							mg_time = str(datetime.strptime((datetime.now()).strftime('%Y-%m-%d ') + str(mg_time), '%Y-%m-%d %H:%M') + timedelta(minutes=timeframe))[11:-3]

							if mg_time in catalogacao[par]:
								catalogacao[par][horario]['mg' + str(i + 1)]['verde'] += catalogacao[par][mg_time]['verde'] + soma['verde']
								catalogacao[par][horario]['mg' + str(i + 1)]['vermelha'] += catalogacao[par][mg_time]['vermelha'] + soma['vermelha']
								catalogacao[par][horario]['mg' + str(i + 1)]['doji'] += catalogacao[par][mg_time]['doji'] + soma['doji']

								catalogacao[par][horario]['mg' + str(i + 1)]['%'] = round(100 * (catalogacao[par][horario]['mg' + str(i + 1)]['verde' if catalogacao[par][horario]['dir'] == 'CALL' else 'vermelha'] / (catalogacao[par][horario]['mg' + str(i + 1)]['verde'] + catalogacao[par][horario]['mg' + str(i + 1)]['vermelha'] + catalogacao[par][horario]['mg' + str(i + 1)]['doji'])))

								soma['verde'] += catalogacao[par][mg_time]['verde']
								soma['vermelha'] += catalogacao[par][mg_time]['vermelha']
								soma['doji'] += catalogacao[par][mg_time]['doji']
							else:
								catalogacao[par][horario]['mg' + str(i + 1)]['%'] = 0

			print('finalizado em ' + str(int(time()) - timer) + ' segundos')
			contador += 1

		print('\n\n')

		for par in catalogacao:
			for horario in sorted(catalogacao[par]):
				ok = False
				if config['tendencia'] == 'Y':
					if catalogacao[par][horario]['tendencia'] >= config['tendencia_porcentagem'] and catalogacao[par][horario]['%'] >= porcentagem:
						ok = True
				if config['tendencia'] == 'y':
					if catalogacao[par][horario]['tendencia'] >= config['tendencia_porcentagem'] and catalogacao[par][horario]['%'] >= porcentagem:
						ok = True

				else:
					if catalogacao[par][horario]['%'] >= porcentagem:
						ok = True
					else:
						for i in range(int(martingale)):
							if catalogacao[par][horario]['mg' + str(i + 1)]['%'] >= porcentagem:
								ok = True
								break

				if ok == True:

					msg = Fore.YELLOW + par + Fore.RESET + ' - ' + horario + ' - ' + (Fore.RED if catalogacao[par][horario]['dir'] == 'PUT ' else Fore.GREEN) + catalogacao[par][horario]['dir'] + Fore.RESET + ' - ' + str(catalogacao[par][horario]['%']) + '% - ' + Back.GREEN + Fore.BLACK + str(catalogacao[par][horario]['verde']) + Back.RED + Fore.BLACK + str(catalogacao[par][horario]['vermelha']) + Back.RESET + Fore.RESET + str(catalogacao[par][horario]['doji'])

					if martingale.strip() != '':
						for i in range(int(martingale)):
							if str(catalogacao[par][horario]['mg' + str(i + 1)]['%']) != 'N/A':
								msg += ' | MG ' + str(i + 1) + ' - ' + str(catalogacao[par][horario]['mg' + str(i + 1)]['%']) + '% - ' + Back.GREEN + Fore.BLACK + str(catalogacao[par][horario]['mg' + str(i + 1)]['verde']) + Back.RED + Fore.BLACK + str(catalogacao[par][horario]['mg' + str(i + 1)]['vermelha']) + Back.RESET + Fore.RESET + str(catalogacao[par][horario]['mg' + str(i + 1)]['doji'])
							else:
								msg += ' | MG ' + str(i + 1) + ' - N/A - N/A'
					print(msg)
					direcao = catalogacao[par][horario]['dir'].strip()
					if config['validar_sinal'] == 'Y':
						if Valida_Sinal(info_binarias, info_digitais, horario, par, data_atual):
							Escreve_Arquivo(arquivo_saida, timeframe, par, horario, direcao, data_atual, martingale)
					if config['validar_sinal'] == 'y':
						if Valida_Sinal(info_binarias, info_digitais, horario, par, data_atual):
							Escreve_Arquivo(arquivo_saida, timeframe, par, horario, direcao, data_atual, martingale)
					else:
						Escreve_Arquivo(arquivo_saida, timeframe, par, horario, direcao, data_atual, martingale)
	input()
except KeyboardInterrupt:
	sys.exit()
