import yaml;
from datetime import datetime
import networkx as nx
import graphviz
import re
from fpdf import FPDF;

arx=input("Choose the file: ")
with open(arx) as f:
        data=yaml.load(f, Loader=yaml.FullLoader)

class Variables:
    def __init__(self, name, fu, nexu):
        self.name=name
        self.firstuse=fu
        self.nextuses=nexu

class PDF(FPDF):
    def header(self):
        if self.page_no()==1:
            #imagen de la portada
            self.image('logo.png', 115, 30, 60, 11, 'png')
            #texto de la portada
            self.set_font('Helvetica', '', 30)
            self.set_xy(50, 35)
            self.cell(100, 100, 'Informació infraestructura', 0, 1, '')
            self.set_xy(50, 48)
            self.cell(100, 100, 'de Xarxa Tecnocampus', 0, 1, '')
            self.set_xy(50, 61)
            self.cell(100, 100, '('+ data['lab'].get('title') +')', 0, 1, '')
            self.set_xy(50, 95)

            #Cojer el mes actual
            now=datetime.now()
            format=now.strftime('%m')
            s=""
            if format=='01': s="Gener"
            if format=='02': s="Febrer"
            if format=='03': s="Març"
            if format=='04': s="Abril"
            if format=='05': s="Maig"
            if format=='06': s="Juni"
            if format=='07': s="Juliol"
            if format=='08': s="Agost"
            if format=='09': s="Septembre"
            if format=='10': s="Octubre"
            if format=='11': s="Novembre"
            if format=='12': s="Decembre" 
            self.cell(100, 100, s +' 2021', 0, 1, '')
        else:
            #imagen header
            self.image('logo.png', 130, 8, 52, 10, 'png')
            #texto header
            self.set_font('Helvetica', '', 10)
            self.cell(18, -5)
            self.cell(0, 10, 'Informació infraestructurada de Xarxa Tecnocampus ('+ data['lab'].get('title') +')', 0, 1, '')
            self.ln(20)

    def footer(self):
        if self.page_no()==1:
            #texto de abajo de la portada
            self.set_font('Helvetica', '', 8)
            self.set_xy(28, 240)
            self.cell(50, 3, 'La informacio continguda en aquest document pot ser de caracter privilegiat y/o confidencial. Qualsevol disseminacio,', 0, 1, '')
            self.set_x(28)
            self.cell(50, 3, 'distribucio o copia d aquest document per qualsevol altre persona diferent als receptors originals queda estrictament', 0, 1, '')
            self.set_x(28)
            self.cell(50, 3, 'prohibida. Si ha rebut aquest document per error, sis plau notifiqui immediatament al emissor i esborri qualsevol copia', 0, 1, '')
            self.set_x(28)
            self.cell(50, 3, 'd aquest document.', 0, 1, '')
        else:
            #pagina actual
            self.set_xy(30, -18)
            self.set_font('Helvetica','', 10)
            self.cell(0, 10, str(self.page_no()), 0, 0, '')

def convertidor(var):
    if var=='n1':
        return 1
    if var == 'n2':
        return 2
    if var == 'n3':
        return 3
    if var == 'n4':
        return 4
    if var == 'n5':
        return 5
    if var == 'n6':
        return 6
    if var == 'n7':
        return 7
    if var == 'n8':
        return 8
    if var == 'n9':
        return 9
    if var == 'n0':
        return 0

def main():

    #PORTADA
    pdf=PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    #dibujar linea amarilla
    pdf.set_draw_color(255, 195, 0)
    pdf.set_line_width(6)
    pdf.line(33, 30, 33, 220)

    #ÍNDICE
    pdf.add_page()
    pdf.set_font('Helvetica','',10)
    pdf.set_xy(23,24)
    pdf.ln(2)
    pdf.cell(13)
    pdf.cell(0,7,'ÍNDEX',0,1,'L',False)

    pdf.ln(8)
    pdf.set_font('Helvetica','',10)
    pdf.cell(15)
    pdf.cell(0,7,'1.- Introducció....................................................................................................................................... 4',0,1,'L',False)
    pdf.ln(3)
    pdf.set_font('Helvetica','',10)
    pdf.cell(20)
    pdf.cell(0,0,'1.1.- Descripció................................................................................................................................ 4',0,1,'L',False)
    pdf.ln(7)
    pdf.cell(20)
    pdf.cell(0,0,'1.2.- Objectius.................................................................................................................................. 4',0,1,'L',False)
    pdf.ln(7)
    pdf.cell(20)
    pdf.cell(0,0,'1.3.- Descripció General de les infraestructures.............................................................................. 4',0,1,'L',False)

    pdf.set_font('Helvetica','',10)
    pdf.ln(7)
    pdf.cell(15)
    pdf.cell(0,0,'2.- Configuració dels Dispositius.......................................................................................................... 4',0,1,'L',False)
    pdf.set_font('Helvetica','',10)

    #índice para cada uno de los nodos
    p=1
    pag=4
    for a in data['nodes']:
        if(p==9):
            pdf.add_page()
        else:
            pdf.ln(7)
        pdf.cell(20)
        if(p==2):
            pag=5
        if(p==3):
            pag=7
        if(p==4):
            pag=8
        if(p==5):
            pag=10
        if(p==7):
            pag=pag+1
        pdf.cell(0,0,'2.'+ str(p) +'.- '+ a['label'] +'............................................................................................................... '+ str(pag),0,1,'L',False)
        q=1
        if "Building configuration..." in a['configuration']:
            pdf.ln(7)
            pdf.cell(23)
            pdf.cell(0,0,'2.'+ str(p) +'.'+ str(q) +'.- Configuració criptogràfica del dispositiu............................................................................ '+ str(pag),0,1,'L',False)
            q=q+1

        if(pag==8):
            pag=pag+1
        pdf.ln(7)
        pdf.cell(23)
        pdf.cell(0,0,'2.'+ str(p) +'.'+ str(q) +'.- Interfícies........................................................................................................................... '+ str(pag),0,1,'L',False)
        q=q+1

        if "Building configuration..." in a['configuration']:
            if(pag==5):
                pag=pag+1
            pdf.ln(7)
            pdf.cell(23)
            pdf.cell(0,0,'2.'+ str(p) +'.'+ str(q) +'.- Configuració dels protocols d`enrutament......................................................................... '+ str(pag),0,1,'L',False)
            q=q+1
            pdf.ln(7)
            pdf.cell(23)
            pdf.cell(0,0,'2.'+ str(p) +'.'+ str(q) +'.- Configuració de Llistes de Control d`Accés....................................................................... '+ str(pag),0,1,'L',False)
            q=q+1
            pdf.ln(7)
            pdf.cell(23)
            pdf.cell(0,0,'2.'+ str(p) +'.'+ str(q) +'.- Configuració de Banners .................................................................................................. '+ str(pag),0,1,'L',False)
            q=q+1

        p=p+1
    
    pdf.ln(7)
    pdf.cell(15)
    pdf.cell(0,0,'3.- Interfícies....................................................................................................................................... '+ str(pag),0,1,'L',False)


    #HOJA 3
    pdf.add_page()
    pdf.set_font('Helvetica', '', 15)
    pdf.set_xy(28, 26)
    pdf.set_text_color(35, 100, 135)
    pdf.write(5, '1.- Introducció')
    pdf.set_font('Helvetica', '', 12)
    pdf.set_xy(28, 32)
    pdf.write(10, '1.1.- Descripció')
    pdf.set_xy(28, 38)
    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(0, 0, 0)
    pdf.write(10, 'El present document descriu la topologia realitzada amb la configuració '+ data['lab'].get('title') +' a la')
    pdf.set_xy(28, 42)
    pdf.write(10, 'empresa TecnoCampus.')
    pdf.ln(8)
    pdf.cell(18)

    pdf.set_font('Helvetica', '', 12)
    pdf.set_text_color(35, 100, 135)
    pdf.cell(10, 10, '1.2.- Objectius', 0, 1)
    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(18)
    pdf.cell(0, 0, 'El objectiu d aquest document és la de formalitzar el traspàs d informació al equip tècnic', 0, 1)
    pdf.ln(4)
    pdf.cell(18)
    pdf.cell(0, 0, 'responsable del manteniment de les infraestructures instal·lades. Aquesta informació fa', 0, 1)
    pdf.ln(4)
    pdf.cell(18)
    pdf.cell(0, 0, 'referencia al disseny, instal·lació i configuració dels dispositius i sistemes afectats per la', 0, 1)
    pdf.ln(4)
    pdf.cell(18)
    pdf.cell(0, 0, 'implementació.', 0, 1)
    pdf.ln(4)
    pdf.cell(18)
    pdf.cell(0, 0, 'La present documentació inclou:', 0, 1)
    pdf.ln(4)
    pdf.cell(23)
    pdf.cell(0, 0, '-   Descripció general de les infraestructures instal·lades.', 0, 1)
    pdf.ln(4)
    pdf.cell(23)
    pdf.cell(0, 0, '-   Configuració de les interfícies de xarxa', 0, 1)
    pdf.ln(4)
    pdf.cell(23)
    pdf.cell(0, 0, '-   Configuració de les polítiques per les connexions VPN', 0, 1)
    pdf.ln(4)
    pdf.cell(23)
    pdf.cell(0, 0, '-   Configuració dels protocols d enrutament', 0, 1)
    pdf.ln(4)
    pdf.cell(23)
    pdf.cell(0, 0, '-   Configuració de les llistes de control d accés', 0, 1)
    pdf.ln(4)
    pdf.cell(23)
    pdf.cell(0, 0, '-   Configuració dels banners', 0, 1)

    pdf.set_font('Helvetica', '', 12)
    pdf.set_text_color(35, 100, 135)
    pdf.ln(1)
    pdf.cell(18)
    pdf.cell(10, 10, '1.3.- Descripció General de les infraestructures', 0, 1)
    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(18)
    pdf.cell(0, 0, 'Actualment la topologia té la següent distribució:', 0, 1)

    #MAPA DE TOPOLOGIA
    g =  nx.Graph()
    nodos = list()
    i=0
    while i < len(data['nodes']):
       nodos.append(data['nodes'][i]['label'])
       g.add_node(data['nodes'][i]['label'])
       i+=1 
   
    linkI = list()
    linkF = list()
    x =0
    while x < len(data['links']):
        linkI.append(data['links'][x]['n1'])
        linkF.append(data['links'][x]['n2'])
        x+=1   
    
    n=0
    while n < len(linkI):
        linkI[n] = convertidor(linkI[n])
        linkF[n] = convertidor(linkF[n])
        n=n+1
    l=0
    while l < len(linkI):
        g.add_edge(nodos[linkI[l]-1],nodos[linkF[l]-1])
        l=l+1
    img = nx.nx_agraph.to_agraph(g)
    img.layout('dot')
    img.draw('pl.jpg')
    pdf.image('pl.jpg', 55, 120, 100, 60, 'jpg')

    pdf.ln(75)
    pdf.cell(18)
    pdf.cell(0, 0, 'En aquesta topologia tenim '+ str(len(g.nodes)) +' equips, connectats a través de '+ str(len(linkI)) +' links', 0, 1)
    pdf.set_font('Helvetica', '', 15)
    pdf.ln(5)
    pdf.cell(18)
    pdf.set_text_color(35, 100, 135)
    pdf.cell(10, 10, '2.- Configuració dels dispositius', 0, 1)
    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(1)
    pdf.cell(18)
    pdf.cell(0, 0, 'A continuació, es detalla la configuració dels diferents dispositius:', 0, 1)
    
    #tractamos cada uno de los nodos
    i=1
    xarxesT= list()
    equip=list()
    interf= list()
    ips= list()
    for a in data['nodes']:
        pdf.set_text_color(35, 100, 135)
        pdf.set_font('Helvetica', '', 12)
        pdf.ln(8)
        pdf.cell(18)
        pdf.cell(0, 0, '2.'+str(i)+'.- '+ a['label'], 0, 1)
        pdf.ln(6)
        pdf.cell(18)
        j=1
        if "Building configuration..." in a['configuration']:
            pdf.set_font('Helvetica', '', 11)
            pdf.set_text_color(0, 0, 0)
            
            #Cojer fecha y hora
            pattern='UTC'
            match=re.search(pattern, a['configuration'])
            s=match.start()
            e=match.end()
            hora=a['configuration'][(s-9):(e)]
            fecha=a['configuration'][(e+5):(e+16)]

            pdf.cell(0, 0, 'El darrer canvi de la configuració va ser el '+ fecha +' a les '+ hora, 0, 1)
            pdf.set_text_color(35, 100, 135)
            pdf.set_font('Helvetica', '', 12)
            pdf.ln(9)
            pdf.cell(18)
            pdf.cell(0, 0, '2.'+ str(i) +'.'+ str(j) +'.- Configuració criptogràfica del dispositiu', 0, 1)
            pdf.set_font('Helvetica', '', 11)
            pdf.set_text_color(0, 0, 0)
            pdf.ln(7)
            pdf.cell(18)
            if "crypto" in a['configuration']:
                pdf.cell(0, 0, 'El dispositiu té la següent configuració de crypto:', 0, 1)
                pdf.ln(9)
                pdf.cell(25)
                
                #Cojer ip
                #buscamos este string en la cadena
                pattern='set peer'
                match=re.search(pattern, a['configuration'])
                e=match.end()
                ip=a['configuration'][(e+1):(e+9)]

                pdf.cell(0, 0, '-    Conexió amb '+ ip +':', 0, 1)
                pdf.ln(6)
                pdf.cell(40)

                #Cojer numero
                pattern='isakmp policy'
                match=re.search(pattern, a['configuration'])
                e=match.end()
                numero=a['configuration'][(e+1):(e+3)]

                pdf.cell(0, 0, 'o   Política de regles número '+ numero +':', 0, 1)
                pdf.ln(6)
                pdf.cell(55)

                #Cojer encript
                pattern='encr aes'
                match=re.search(pattern, a['configuration'])
                e=match.end()
                encript=a['configuration'][(e-3):(e+4)]

                pdf.cell(0, 0, '·    Encriptació '+ encript, 0, 1)
                pdf.ln(6)
                pdf.cell(55)

                #Cojer authentification
                pattern='authentication'
                match=re.search(pattern, a['configuration'])
                e=match.end()
                auth=a['configuration'][(e+1):(e+10)]

                pdf.cell(0, 0, '·    Autenticació '+ auth, 0, 1)
                pdf.ln(6)
                pdf.cell(55)

                #Cojer group
                pattern='group'
                match=re.search(pattern, a['configuration'])
                e=match.end()
                group=a['configuration'][(e+1)]

                pdf.cell(0, 0, '·    Diffie-Helmann grup '+ group, 0, 1)
                pdf.ln(6)
                pdf.cell(40)

                #Cojer key
                pattern='isakmp key'
                match=re.search(pattern, a['configuration'])
                e=match.end()
                key=a['configuration'][(e+1):(e+8)]

                pdf.cell(0, 0, 'o   Contrasenya ISAKMP: '+ key, 0, 1)
                pdf.ln(6)
                pdf.cell(40)
                pdf.cell(0, 0, 'o   Configuració VPN:', 0, 1)
                pdf.ln(6)
                pdf.cell(55)

                #Cojer tranform
                pattern='ipsec transform-set'
                match=re.search(pattern, a['configuration'])
                e=match.end()
                transform=a['configuration'][(e+1):(e+4)]
                
                pdf.cell(0, 0, '·    Conjunt de transformació '+ transform, 0, 1)
                pdf.ln(6)
                pdf.cell(55)

                #Cojer encriptaci
                encriptaci=a['configuration'][(e+5):(e+12)]

                pdf.cell(0, 0, '·    Configuració Encriptació ESP: '+ encriptaci, 0, 1)
                pdf.ln(6)
                pdf.cell(55)

                #Cojer signatur
                signatur=a['configuration'][(e+13):(e+25)]

                pdf.cell(0, 0, '·    Configuració Signatura ESP: '+ signatur, 0, 1)
                pdf.ln(6)
                pdf.cell(55)

                #Cojer mode
                mod=a['configuration'][(e+32):(e+38)]

                pdf.cell(0, 0, '·    Mode '+ mod, 0, 1)
                pdf.ln(6)
                pdf.cell(55)

                #Cojer acl
                pattern='match address'
                match=re.search(pattern, a['configuration'])
                e=match.end()
                acl=a['configuration'][(e+1):(e+4)]

                pdf.cell(0, 0, '·    ACL número '+ acl, 0, 1)
            else:
                pdf.cell(0, 0, 'El dispositiu no té configuració de crypto', 0, 1)
            
            j=j+1

        pdf.set_text_color(35, 100, 135)
        pdf.set_font('Helvetica', '', 12)
        if "Building configuration..." in a['configuration']:
            pdf.ln(8)
            pdf.cell(18)
        pdf.cell(0, 0, '2.'+ str(i) +'.'+ str(j) +'.- Interfícies', 0, 1)
        pdf.set_font('Helvetica', '', 11)
        pdf.set_text_color(0, 0, 0)
        pdf.ln(7)
        pdf.cell(18)
        pdf.cell(0, 0, 'Les interfícies i la seva configuració és:', 0, 1)
        pdf.ln(9)

        for b in a['interfaces']:
            pdf.cell(25)

            #Cojer las ip
            pattern=b['label']
            match=re.search(pattern, a['configuration'])
            ipAddr=''
            if match!=None:
                e=match.end()
                if "no" not in a['configuration'][(e):(e+5)]:
                    ipAddr=a['configuration'][(e+13):(e+38)]
                    pattern='255.255'
                    match=re.search(pattern, ipAddr)
                    if match != None:
                        s=match.start()
                        equip.append(a['label'])
                        interf.append(b['id'])
                        ips.append(ipAddr[:s])

                        ipAddr=': '+ipAddr[:s]+'('+ipAddr[s:len(ipAddr)]+')'
                
                if 'alpine' in a['node_definition']:
                    equip.append(a['label'])
                    interf.append(b['id'])

                    ipAddr=' (DG: '+ipAddr[13:]+')'
                    pattern='ip addr add'
                    match=re.search(pattern, a['configuration'])
                    e=match.end()
                    ips.append(a['configuration'][(e+1):(e+12)])

                    ipAddr='. Configuració IP: '+a['configuration'][(e+1):(e+15)]+ ipAddr
            
            pdf.cell(0, 0, '-    Link '+ b['id']+': '+ b['label']+ ipAddr, 0, 1)
            pdf.ln(5)
        j=j+1

        if "Building configuration..." in a['configuration']:
            pdf.set_text_color(35, 100, 135)
            pdf.set_font('Helvetica', '', 12)
            pdf.ln(5)
            pdf.cell(18)
            pdf.cell(0, 0, '2.'+ str(i) +'.'+ str(j) +'.- Configuració dels protocols d enrutament', 0, 1)
            pdf.set_font('Helvetica', '', 11)
            pdf.set_text_color(0, 0, 0)
            pdf.ln(7)
            pdf.cell(18)

            #Cojer protocol
            pattern='router ospf'
            match=re.search(pattern, a['configuration'])
            if(match!=None):
                e=match.end()
            protocol=a['configuration'][(e-4):(e+4)]

            pdf.cell(0, 0, 'El protocol d enrutament utilitzat és '+ protocol.upper() +', amb la següent configuració (xarxes publicades):', 0, 1)
            pdf.ln(7)
            pdf.cell(25)

            #Cojer area
            pattern='area'
            match=re.search(pattern, a['configuration'])
            if(match!=None):
                e=match.end()
            area=a['configuration'][e+1]

            pdf.cell(0, 0, '-    Àrea '+ area+':', 0, 1)


            #Cojer network
            pattern='network'
            match=re.search(pattern, a['configuration'])
            if(match!=None):
                s=match.end()

            s=s+1
            network=""
            while a['configuration'][s]!='!':
                network=network+a['configuration'][s]
                s=s+1

            num=a['configuration'].count("area")
            network=network.replace("network", "")
            network=network.replace("area 0", "")

            while num>0:
                pattern=' '
                match=re.search(pattern, network)
                if(match!= None):
                    x=match.end()
                    if network[:x-1] not in xarxesT:
                        xarxesT.append(network[:x-1])
                    parte1=network[:x-1]+' màscara invertida '
                    network=network[x:]
                    network=network[2:]
                    match=re.search(pattern, network)
                    parte2=network[:x-1]
                    network=network[x:]
                    net=parte1+parte2

                pdf.ln(5)
                pdf.cell(40)
                pdf.cell(0, 0, 'o   Xarxa '+ net, 0, 1)

                num=num-1 
            
            j=j+1

        if "Building configuration..." in a['configuration']:
            pdf.set_text_color(35, 100, 135)
            pdf.set_font('Helvetica', '', 12)
            pdf.ln(9)
            pdf.cell(18)
            pdf.cell(0, 0, '2.'+ str(i) +'.'+ str(j) +'.- Configuració de Llistes de Control d Accés', 0, 1)
            pdf.set_font('Helvetica', '', 11)
            pdf.set_text_color(0, 0, 0)
            pdf.ln(7)
            pdf.cell(18)
            if "access-list" in a['configuration']:
                pdf.cell(0, 0, 'El dispositiu té configurada la següent ACL:', 0, 1)
                pdf.ln(7)
                pdf.cell(25)

                #Cojer acclist
                pattern='access-list'
                match=re.search(pattern, a['configuration'])
                e=match.end()
                acclist=a['configuration'][(e+1):(e+4)]

                pdf.cell(0, 0, '-    Número '+acclist, 0, 1)
                pdf.ln(5)
                pdf.cell(40)

                #Cojer permit
                pattern='permit'
                match=re.search(pattern, a['configuration'])
                e=match.end()
                permit=a['configuration'][(e+1):(e+3)]

                pdf.cell(0, 0, 'o   PERMIT ('+ permit.upper() +'):', 0, 1)
                pdf.ln(5)
                pdf.cell(55)

                #Cojer origen y desti
                pattern='control-plane'
                match=re.search(pattern, a['configuration'])
                s=match.start()
                origdest=a['configuration'][(e+4):(s-2)]
                pattern=' '
                match=re.search(pattern, origdest)
                if(match!= None):
                    x=match.end()
                    origen=origdest[:x-1]+' màscara invertida '+origdest[x:x+9]
                    origdest=origdest[x:]
                    match=re.search(pattern, a['configuration'])
                    x=match.start()
                    origdest=origdest[x+2:]
                    match=re.search(pattern, a['configuration'])
                    x=match.start()
                    desti=origdest[:x+3]+' màscara invertida '+origdest[x+3:x+13]

                pdf.cell(0, 0, '·   ORIGEN: '+origen, 0, 1)
                pdf.ln(5)
                pdf.cell(55)
                pdf.cell(0, 0, '·   DESTÍ: '+desti, 0, 1)
            else:
                pdf.cell(0, 0, 'El dispositiu no té configurada cap ACL.', 0, 1)

            j=j+1

        if "Building configuration..." in a['configuration']:
            pdf.set_text_color(35, 100, 135)
            pdf.set_font('Helvetica', '', 12)
            pdf.ln(9)
            pdf.cell(18)
            pdf.cell(0, 0, '2.'+ str(i) +'.'+ str(j) +'.- Configuració de Banners', 0, 1)
            pdf.set_font('Helvetica', '', 11)
            pdf.set_text_color(0, 0, 0)
            pdf.ln(7)
            pdf.cell(18)
            pdf.cell(0, 0, 'El dispositiu té configurats els següent Banners:', 0, 1)
            pdf.ln(7)

            #Cojer banner
            pattern='banner'
            match=re.search(pattern, a['configuration'])
            e=match.end()
            pattern='line con 0'
            match=re.search(pattern, a['configuration'])
            s=match.start()
            banner=a['configuration'][(e+1):(s-2)]
            banner="    -    "+banner
            banner=banner.replace("banner", "    -    ")
            banner=banner.replace("^CCC", " ")
            banner=banner.replace("^C", " ")
            pdf.cell(18)
            pdf.multi_cell(170, 8, banner, 0, 'J', False)

            j=j+1

        i=i+1

    #PARTE 3
    pdf.set_font('Helvetica', '', 15)
    pdf.ln(5)
    pdf.cell(18)
    pdf.set_text_color(35, 100, 135)
    pdf.cell(10, 10, '3.- Interfícies', 0, 1)
    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(3)
    pdf.cell(18)
    pdf.cell(0, 0, 'La configuració de les interfícies (links) d interconnexió entre equips és:', 0, 1)
    pdf.ln(8)
    for a in data['links']:
        pdf.cell(25)
        pdf.set_font('Helvetica', 'B', 11)

        #Cojer id
        ids='1'+a['id'][1]

        pdf.cell(0, 0, '-    Link '+ids, 0, 1)
        pdf.set_font('Helvetica', '', 11)
        pdf.cell(44)

        #Cojer nombres label con su id
        lab1=''
        lab2=''
        for b in data['nodes']:
            if a['n1'] == b['id']:
                lab1=b['label']
            if a['n2'] == b['id']:
                lab2=b['label']

        pdf.cell(0, 0, ': conecta '+ a['i1'] +' ('+ lab1 +')'+' amb '+ a['i2']+' ('+ lab2 +')', 0, 1)
        pdf.ln(5)

    pdf.ln(3)
    pdf.cell(18)
    pdf.cell(0, 0, 'El resum de les adreces IP de les interfícies és:', 0, 1)

    #TABLA
    pdf.ln(5)
    pdf.cell(13)
    if len(xarxesT)!=0:
        pdf.cell(23, 10, "Xarxa", 0, 0)
    pdf.cell(23, 10, "Equip1", 0, 0)
    pdf.cell(23, 10, "Interfície1", 0, 0)
    pdf.cell(23, 10, "IP1", 0, 0)
    pdf.cell(23, 10, "Equip2", 0, 0)
    pdf.cell(23, 10, "Interfície2", 0, 0)
    pdf.cell(23, 10, "IP2", 0, 0)
    pdf.ln(6)

    l=0
    while l< len(equip):
        pdf.cell(13)
        if len(xarxesT)!=0:
            if l==0:
                pdf.cell(23, 10, xarxesT[l], 0, 0)
            else:
                pdf.cell(23, 10, xarxesT[int(l/2)], 0, 0)
        pdf.cell(23, 10, equip[l], 0, 0)
        pdf.cell(23, 10, interf[l], 0, 0)
        pdf.cell(23, 10, ips[l], 0, 0)
        if(l+1!=len(equip)):
            pdf.cell(23, 10, equip[l+1], 0, 0)
            pdf.cell(23, 10, interf[l+1], 0, 0)
            pdf.cell(23, 10, ips[l+1], 0, 0)
            pdf.ln(5)
        else:
            pdf.ln(5)
        
        l=l+2

    #GUARDAR
    tie=data['lab'].get('title')
    pdf.output(tie+'.pdf', 'F')


if __name__ == "__main__":
    main()