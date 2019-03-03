# coding=utf8
from selenium import webdriver
import time
import sys
import csv
import pandas as pd

#declaração de variáveis
correio = "https://www2.correios.com.br/sistemas/rastreamento/default.cfm"
qtdd_codigos = ""
codigos = []
status = []
datas = []
locais = []

#loop básico para receber a quantidade de códigos que serão utilizados durante a execução
while type(qtdd_codigos) != int:
    print("Quantos códigos você quer colocar? (Responda com números - Ex: 1)")
    try:
        qtdd_codigos = int(input("---> "))
    except:
        print("Por favor, coloque um valor numérico.")

if qtdd_codigos == 0:
    print("A quantidade inserida foi %s" %qtdd_codigos)
    print("Não há nada que possamos fazer... Fechando em 3 segundos.")
    time.sleep(3)
    sys.exit()

#cechagem da quantidade de códigos
if qtdd_codigos == 1:
    resposta = input("Digite o código desejado: ")
    driver = webdriver.PhantomJS('C:/Users/Cristian/Desktop/Rastreio_Correio/correio/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get(correio)

    codigos_escrever = driver.find_element_by_xpath('//*[@id="objetos"]')
    codigos_escrever.clear()
    codigos_escrever.send_keys(resposta + ";")

    buscar = driver.find_element_by_xpath('//*[@id="btnPesq"]')
    buscar.click()

    ultimo_status = driver.find_element_by_xpath('/html/body /div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/strong').text
    print("Para o código %s, o último status encontrado foi: %s" % (resposta, ultimo_status))

    driver.close()
#checagem da quantidade de códigos
if qtdd_codigos > 1:
    #print("Digite os códigos desejados:")
    #for i in range(qtdd_codigos):
    #    resposta = input(str(int(i+1)) + "º --> ")
     #   codigos.append(resposta)
     #   i+=1

    driver = webdriver.PhantomJS('C:/Users/Cristian/Desktop/Rastreio_Correio/correio/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get(correio)
    codigos = ["PS290365926BR","PS290252456BR","PS290160746BR","PS290123173BR","PS290328605BR","PS290489038BR","PS290384531BR","PS290600451BR","PS290124752BR","PS290439266BR","PS290239790BR","PS290298651BR","PS290392325BR","PS290135888BR","OG355401474BR","PS290293447BR","PS290377385BR","PS290188191BR","PS290388578BR","PS290210411BR","PS290537025BR","PS290363735BR","PS290536444BR","OG355438823BR","PP965073647BR","PS290351873BR","PS290297506BR","PS290167435BR","PS290317727BR","PS290209665BR","PS290220921BR","PS290255996BR","PP965142360BR","PS290446885BR","PS290152170BR","PS290279459BR","PS290120720BR","PS290134485BR","PP965161298BR","PS290123350BR","OG673435985BR","OG673421005BR","PS290276347BR","PS290116552BR","OG355572575BR","PS290333747BR","PS290536651BR","PS290393697BR","PS290150995BR","PS290176335BR","PS290281996BR","PS290464861BR","PS290397844BR","PS290400367BR","PS290514421BR","PS290374401BR","PS290345294BR","PS290460462BR","PS290363196BR","OG673717575BR","PS290293521BR","PS290409661BR","PS290266203BR","OG673363458BR","PS290141490BR","PS290366816BR","OG355831346BR","PS290358390BR","PS290572305BR","PS290532513BR","PP965152296BR","OG673730599BR","PS290470822BR","PS290451770BR","OG673737699BR","PS290194501BR","PS290394879BR","OG355515128BR","PS290379576BR","PS290459190BR","PS290502627BR","PS290486235BR","PS290140401BR","PS290135242BR","PS290285352BR","PS290286534BR","PS290421883BR","PS290339563BR","PS290348463BR","PS290507876BR","PS290526570BR","PS290228430BR","PS290460459BR","PS290305247BR","OG673304260BR","OG355432370BR","PS290121708BR","PS290471876BR","PS290348640BR","PS290391869BR","OG355580360BR","PS290346502BR","PS290499667BR","PS290284017BR","PS290532178BR","PS290540214BR","PS290345524BR","PS290465685BR","OG355608730BR","PS290536798BR","PS290277648BR","PS290411625BR","PS290591953BR","PS290585269BR","PS290247385BR","PS290528403BR","PS290417402BR","PS290215498BR","OG673520944BR","OG355529113BR","PS290541356BR","PS290522547BR","OG673264217BR","OG355552545BR","OG673622268BR","OG673521026BR","OG355490443BR","OG673525924BR","PS290292849BR","OG673695543BR","OG355442831BR","OG673474290BR","OG355808444BR","OG355773161BR","OG673575660BR","OG673695605BR","PS290406546BR","OG673684846BR","OG673342532BR","OG673348552BR","OG673400337BR","OG673270022BR","PS290257643BR","PS290213611BR","OG355729928BR","PS290363409BR","OG673675929BR","PS290345382BR","OG355392891BR","OG673551751BR","OG355643073BR","OG355745832BR","OG355636090BR","OG673390095BR","OG673440163BR","OG673293995BR","OG673676204BR","OG673753586BR","PS290430911BR","OG355691856BR","PS290478392BR","OG355438117BR","OG355560816BR","OG673704673BR","PS290547654BR","PS290471350BR","OG355686255BR","PS290521997BR","OG673415288BR","PS290444235BR","OG673565716BR","OG355850005BR","OG355671715BR","PS290438835BR","OG355835918BR","OG673418315BR","OG673666745BR","OG355834719BR","PS290351286BR","OG673517993BR","OG673404753BR","OG355586813BR","PS290485288BR","PS290296298BR","OG673421650BR","PS290531711BR","PS290309535BR","OG673594006BR","OG355387106BR","PS290235912BR","OG355597144BR","OG673680844BR","OG673465390BR","PS290306018BR","OG673427309BR","OG673318480BR","PS290486748BR","OG673613527BR","OG673718289BR","PS290296797BR","PS290344237BR","PS290150151BR","OG673303030BR","OG673718955BR","OG673672074BR","OG673475088BR","PS290317262BR","PS290534253BR","OG673727674BR","OG673319922BR","PS290362301BR","PS290202993BR","PS290560275BR","PS290397708BR","OG355718620BR","OG355573355BR","OG673606092BR","OG355689716BR","PS290512709BR","OG355722434BR","OG673606248BR","OG673587402BR","OG355450930BR","PS290559533BR","PS290452316BR","OG355620846BR","PS290202741BR","OG355426357BR","OG355484289BR","PS290279122BR","OG673407485BR","OG673414720BR","PS290309399BR","PS290237238BR","OG355648813BR","PS290464040BR"]

    codigos_escrever = driver.find_element_by_xpath('//*[@id="objetos"]')
    codigos_escrever.clear()

    if len(codigos) <= 50:
        for i in codigos:
            codigos_escrever.send_keys(i + ";")
    else:
        for a in range(0,1000):
            driver.get(correio)
            x = 50*a
            y = 50 + x
            if x>len(codigos):
                driver.close()
                break
            while y < (len(codigos))*2 :
                try:
                    codigos_escrever = driver.find_element_by_xpath('//*[@id="objetos"]')
                    codigos_escrever.clear()
                    for i in codigos[x:y]:
                        codigos_escrever.send_keys(i + ";")
                    buscar = driver.find_element_by_xpath('//*[@id="btnPesq"]')
                    buscar.click()

                    for i in range(len(codigos[x:y])):
                        """if i%50:
                            pass
                        else:"""
                        print(i+x)
                        try:
                            ultimo_status_i = driver.find_element_by_xpath('//*[@id="sroFormMultiResultado"]/table/tbody/tr[' + str(i + 1) + ']/td[3]/b').text
                            status.append(ultimo_status_i)
                            data_local = driver.find_element_by_xpath('//*[@id="sroFormMultiResultado"]/table/tbody/tr['+ str(i+1) +']/td[4]').text

                            dates = data_local.split(' ')
                            data = dates[0]
                            datas.append(data)
                            local = data_local.replace(data,"")
                            locais.append(local)

                            print("Código: %s ---- Status: %s ---- Data: %s --- Local: %s" % (codigos[i + x], status[-1], datas[-1], locais[-1]))
                        except Exception as erro:
                            ultimo_status_i = 'Status não encontrado'
                            status.append(ultimo_status_i)
                            data = 'N/A'
                            local = 'N/A'
                            datas.append(data)
                            locais.append(local)
                            print("Código: %s ---- Status: %s ---- Data: %s --- Local: %s" % (codigos[i + x], status[-1], datas[-1], locais[-1]))
                            pass

                except Exception as erro:
                    break

#cria um arquivo .csv com todos os resultados.
with open('resultado_rastreio.csv', 'w') as resultado:
    colunas = ['Codigo', 'Status_Rastreio', 'Data', 'Local']
    writer = csv.DictWriter(resultado, fieldnames=colunas)
    writer.writeheader()
    for i in range(len(codigos)):
        try:
            writer.writerow({'Codigo': codigos[i], 'Status_Rastreio': status[i], 'Data': datas[i], 'Local': locais[i]})
        except:
            break
df = pd.read_csv('resultado_rastreio.csv', encoding='windows-1252')
print(df.head())