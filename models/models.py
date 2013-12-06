
prov_empresa = db.define_table("prov_empresa",
	Field("proxy", length=30),
	Field("dns", length=30),
	Field("ntp", length=30),
	Field("empresa", length=30),
	format 	=	"%(empresa)s",
	migrate	=	False)

prov_equipamento = db.define_table("prov_equipamento",
	Field("fabricante", length=30),
	Field("modelo", length=30),
	Field("linha", "integer", notnull=True, length=2),
	format	=	"%(modelo)s",
	migrate	=	False)

prov_mac 	=	 db.define_table("prov_mac",
	Field("id_equipamento", db.prov_equipamento),
	Field("id_empresa", db.prov_empresa),
	Field("mac", length=30),
	Field("ip", length=30),
	Field("mascara", length=30),
	Field("gateway", length=30),
	Field("vlan", length=30),
	format	=	"%(mac)s",
	migrate	=	False)

prov_ramal 	= 	db.define_table("prov_ramal",
	Field("id_mac", db.prov_mac),
	Field("ramal", length=4),
	Field("linha", "integer", length=11),
	migrate	=	False)






