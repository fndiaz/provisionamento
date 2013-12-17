##Agenda
#db.agenda.empresa.requires = IS_NOT_EMPTY(error_message=
#						T("valor não pode ser nulo"))

#db.agenda.telefone.requires = [IS_NOT_EMPTY(error_message=T("o telefone deve conter de 9 a 11 números")),
#IS_NOT_IN_DB(db, 'agenda.telefone', error_message=T("este número está em uso")),
#IS_LENGTH(minsize=9, maxsize=11, error_message=T("o telefone deve conter de 9 a 11 números")),
#IS_MATCH('[0-9]+', error_message=T("somente números"))]

##MAC
db.prov_mac.id_equipamento.requires=IS_IN_DB(
	db, 'prov_equipamento.id','prov_equipamento.modelo', 
    error_message=e_m['in_db'])

db.prov_mac.id_empresa.requires=IS_IN_DB(
	db, 'prov_empresa.id','prov_empresa.empresa', 
    error_message=e_m['in_db'])

db.prov_mac.mac.requires=[
	IS_NOT_EMPTY(
		error_message=T("valor não pode ser nulo")),
	IS_NOT_IN_DB(db, 'prov_mac.mac', 
    	error_message=e_m['not_in_db']),
	IS_LENGTH(minsize=12, maxsize=12, 
		error_message=T("12 números")),
	IS_LOWER(),
]

##RAMAL
db.prov_ramal.id_mac.requires=IS_IN_DB(
	db, 'prov_mac.id','prov_mac.mac', 
    error_message=e_m['in_db'])