# coding=UTF-8
import os, commands

## --------------------------------Empresa
def empresa():
	response.title = 'empresa'
	empresa =	db(db.prov_empresa).select(orderby=db.prov_empresa.id)

	return response.render("initial/empresa.html", 
		empresa=empresa)

def edit_empresa():
	response.title = ' editar empresa'
	id_emp 	=	request.vars['id_emp']
	empresa = 	db(db.prov_empresa.id == id_emp).select()
	empresa = 	empresa[0]

	return response.render("initial/edit_empresa.html", 
		empresa=empresa, id_emp=id_emp)

def add_empresa():
	response.title = ' add empresa'
	return response.render("initial/add_empresa.html")


## --------------------------------Equipamneto
def equipamento():
	response.title = 'equipamento'
	equip 	=	db(db.prov_equipamento).select(
					orderby=db.prov_equipamento.id)
	print equip
	return response.render("initial/equipamento.html", 
		equip=equip)

def edit_equipamento():
	response.title = 'editar equipamento'
	id_equip=	request.vars['id_equip']
	equip 	=	db(db.prov_equipamento.id == id_equip).select()
	equip 	=	equip[0]

	return response.render("initial/edit_equipamento.html", 
		equip=equip, id_equip=id_equip)

def add_equipamento():
	response.title = ' add equipamento'
	return response.render("initial/add_equipamento.html")


## --------------------------------Mac
def mac():
	response.title = 'mac address'
	query 	=	(db.prov_empresa.id == db.prov_mac.id_empresa)\
		 & (db.prov_equipamento.id == db.prov_mac.id_equipamento)		
	paginate 	=	10
	if not request.vars.page:
		redirect(URL(vars={'page':1}))
	else:
		page 	=	int(request.vars.page)
	start 	=	(page-1)*paginate
	end 	=	page*paginate
	regis 	=	db(query).count()
	x=1
	if regis%paginate == 0:
		x=0

	mac = db(query).select(db.prov_mac.id, db.prov_mac.id_equipamento, 
		db.prov_equipamento.modelo, db.prov_mac.id_empresa, 
		db.prov_empresa.empresa, db.prov_mac.mac, db.prov_mac.ip, 
		db.prov_mac.gateway, db.prov_mac.vlan, 
		orderby=db.prov_equipamento.modelo, limitby=(start,end))
	print mac

	return response.render("initial/mac.html", mac=mac, end=end,
				paginacao='on', regis=regis, paginate=paginate, x=x)

def edit_mac():
	response.title = 'editar mac address'
	id_mac 	= 	request.vars['id_mac']
	form 	=	SQLFORM(db.prov_mac, id_mac, 	
						submit_button = 'Editar')
	if form.process().accepted:
		#response.flash = 'ok'
		redirect(URL('mac'))

	return response.render("initial/add_mac.html", form=form)


def add_mac():
	response.title = 'add mac address'
	form 	=	SQLFORM(db.prov_mac, 
						submit_button = 'Adicionar')
	form.element(_name='id_equipamento')['_class'] = "form-control"
	if form.process().accepted:
		#response.flash = 'ok'
		redirect(URL('mac'))

	return response.render("initial/add_mac.html", form=form)


## --------------------------------Ramal
def ramal():
	response.title = 'ramal'
	query 	=	db.prov_ramal.id_mac == db.prov_mac.id
	paginate 	=	10
	if not request.vars.page:
		redirect(URL(vars={'page':1}))
	else:
		page 	=	int(request.vars.page)
	start 	=	(page-1)*paginate
	end 	=	page*paginate
	regis 	=	db(query).count()
	x=1
	if regis%paginate == 0:
		x=0

	ramal=db(query)\
		.select(db.prov_mac.mac, db.prov_ramal.id, 
		db.prov_ramal.ramal, db.prov_ramal.linha, 
		orderby=[db.prov_mac.mac, db.prov_ramal.linha],
		limitby=(start,end))
	
	return response.render("initial/ramal.html", ramal=ramal, 
	paginacao='on', end=end, regis=regis, paginate=paginate, x=x)

def edit_ramal():
	response.title = 'editar ramal'
	id_ramal=	request.vars['id_ramal']
	form 	= 	SQLFORM(db.prov_ramal, id_ramal,
							submit_button = 'Editar')
	if form.process().accepted:
		com = commands.getoutput(
		"php /aldeia/script/asterisk/provisionamento.php")
		print com
		redirect(URL('ramal'))

	return response.render("initial/add_ramal.html", form=form)

def add_ramal():
	response.title = 'add ramal'
	form 	=	SQLFORM(db.prov_ramal, 
						submit_button = 'Adicionar')
	if form.process().accepted:
		com = 	commands.getoutput(
		"php /aldeia/script/asterisk/provisionamento.php")
		print com
		redirect(URL('ramal'))

	return response.render("initial/add_ramal.html", form=form)

## --------------------------------acao empresa
def update_empresa():
	id_emp	=	request.vars['id_emp']
	empresa = 	request.vars['empresa']
	proxy	= 	request.vars['proxy']
	dns		=	request.vars['dns']
	ntp		=	request.vars['ntp']
	db(db.prov_empresa.id == id_emp).update(
		empresa=empresa, proxy=proxy, dns=dns, ntp=ntp)

	redirect(URL('empresa'))

def insert_empresa():
	empresa = 	request.vars['empresa']
	proxy	= 	request.vars['proxy']
	dns		=	request.vars['dns']
	ntp		=	request.vars['ntp']
	db.prov_empresa.insert(
		empresa=empresa, proxy=proxy, dns=dns, ntp=ntp)

	redirect(URL('empresa'))

def delete_empresa():
	id_emp 	=	request.vars['id_emp']
	db(db.prov_empresa.id == id_emp).delete()

	redirect(URL('empresa'))


## ---------------------------------acao equipamento
def update_equipamento():
	id_equip=	request.vars['id_equip']
	fabric 	=	request.vars['fabricante']
	modelo 	=	request.vars['modelo']
	linha 	=	request.vars['linha']
	db(db.prov_equipamento.id == id_equip).update(
		fabricante=fabric, modelo=modelo, linha=linha)

	redirect(URL('equipamento'))

def insert_equipamento():
	fabric 	=	request.vars['fabricante']
	modelo 	=	request.vars['modelo']
	linha 	=	request.vars['linha']
	db.prov_equipamento.insert(
		fabricante=fabric, modelo=modelo, linha=linha)

	redirect (URL('equipamento'))

def delete_equipamento():
	id_equip=	request.vars['id_equip']
	db(db.prov_equipamento.id == id_equip).delete()

	redirect(URL('equipamento'))

## ---------------------------------acao mac
def delete_mac():
	id_mac 	=	request.vars['id_mac']
	db(db.prov_mac.id == id_mac).delete()

	redirect(URL('mac'))

def json_mac():
	ramal 	= 	db(db.prov_mac)\
	.select(db.prov_mac.mac)
	lista 	=	[]
	for dado in ramal:
		lista.append(dado.mac)
	lista 	=	list(set(lista))
	return response.json(lista)

def busca_mac():
	response.title	=	'mac'
	busca 	=	request.vars['nome']		
	query	=	(db.prov_empresa.id == db.prov_mac.id_empresa)\
		& (db.prov_equipamento.id == db.prov_mac.id_equipamento)\
				& (db.prov_mac.mac.like('%'+busca+'%'))
	
	if db(query).count() > 0:
		mac=db(query).select(db.prov_mac.id, db.prov_mac.id_equipamento, 
		db.prov_equipamento.modelo, db.prov_mac.id_empresa, 
		db.prov_empresa.empresa, db.prov_mac.mac, db.prov_mac.ip, 
		db.prov_mac.gateway, db.prov_mac.vlan, 
		orderby=db.prov_equipamento.modelo)
	else:
		session.flash = 'nenhuma busca encontrada'
		redirect(URL('mac'))
	
	return response.render("initial/mac.html", mac=mac,
											paginacao='off')

## ---------------------------------acao ramal
def delete_ramal():
	id_ramal	=	request.vars['id_ramal']

	mac=db((db.prov_ramal.id == id_ramal) &\
	(db.prov_ramal.id_mac == db.prov_mac.id))\
	.select(db.prov_mac.mac)
	mac 	=	str(mac[0].mac).lower()

	com = commands.getoutput(
	"rm -f /var/www/provisionamento/%s.cfg" %(mac))
	print com

	db(db.prov_ramal.id == id_ramal).delete()
	com2 = 	commands.getoutput(
	"php /aldeia/script/asterisk/provisionamento.php") 

	redirect(URL('ramal'))

def json_ramal():
	ramal 	= 	db(db.prov_mac.id == db.prov_ramal.id_mac)\
	.select(db.prov_mac.mac)
	lista 	=	[]
	for dado in ramal:
		lista.append(dado.mac)
	lista 	=	list(set(lista))
	return response.json(lista)

def busca_ramal():
	response.title	=	'ramal'
	busca 	=	request.vars['nome']		
	query	=	((db.prov_ramal.id_mac == db.prov_mac.id)\
				 & (db.prov_mac.mac.like('%'+busca+'%')))\
			| ((db.prov_ramal.id_mac == db.prov_mac.id)\
				 & (db.prov_ramal.ramal.like('%'+busca+'%')))
	
	if db(query).count() > 0:
		ramal=db(query).select(db.prov_mac.mac, db.prov_ramal.id, 
				db.prov_ramal.ramal, db.prov_ramal.linha,
				orderby=[db.prov_mac.mac, db.prov_ramal.linha])
	else:
		session.flash = 'nenhuma busca encontrada'
		redirect(URL('ramal'))
	
	return response.render("initial/ramal.html", ramal=ramal,
											  paginacao='off')


def principal():
	redirect(URL('empresa'))









def user():
	#if request.args(0) == 'register':
    #    	db.auth_user.bio.writable = db.auth_user.bio.readable = False
	return response.render("initial/user.html", user=auth())

def register():
	return auth.register()

def login():
        return auth.login()

def account():
    return dict(register=auth.register(),
                login=auth.login())
	
def download():
	return response.download(request, db)

def log():
	response.title = 'Padrão'
	#grid = SQLFORM.grid(db.prov_empresa,
	#	user_signature=False, searchable=True, create=True, csv=False, 
    #           paginate=10, details=False)

	#prov_empresa = db(db.prov_ramal).select(orderby=db.prov_ramal.id)
	update = db.prov_empresa(request.args())
	form = SQLFORM(db.prov_empresa, update)
	
	return response.render("initial/show_form2.html", form=form)



	



