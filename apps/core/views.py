from django.shortcuts import render

presidentes = [
    {
        "id": 1,
        "nombre": "Raúl Ricardo Alfonsín",
        "periodo": "1983 - 1989",
        "url": "alfonsin",
    },
    {"id": 2, "nombre": "Carlos S. Menem", "periodo": "1989 - 1999", "url": "menem"},
    {
        "id": 3,
        "nombre": "Fernando De la Rúa",
        "periodo": "1999 - 2001",
        "url": "delarua",
    },
    {
        "id": 4,
        "nombre": "Puerta Rodriguez Saá Camaño",
        "periodo": "2001 - 2002",
        "url": "puerta rodriguez camaño",
    },
    {"id": 5, "nombre": "Eduardo Duhalde", "periodo": "2002 - 2003", "url": "duhalde"},
    {"id": 6, "nombre": "Néstor Kirchner", "periodo": "2003 - 2007", "url": "nestork"},
    {
        "id": 7,
        "nombre": "Cristina Fernández de Kirchner",
        "periodo": "2007 - 2015",
        "url": "cristinak",
    },
    {"id": 8, "nombre": "Mauricio Macri", "periodo": "2015 - 2019", "url": "macri"},
    {
        "id": 9,
        "nombre": "Alberto Fernández",
        "periodo": "2019 - 2023",
        "url": "albertofernandez",
    },
    {
        "id": 10,
        "nombre": "Javier Milei",
        "periodo": "2023 - actualidad",
        "url": "milei",
    },
]


fichas = [
    {
        "id": "1",
        "fuente": "Rapoport, M. Año 2000. Historia Política, económica y social de la Argentina. Editorial Macchi",
        "tipoRecurso": "Obras monográficas, libro.",
        "claseFuente": "secundaria",
        "palabrasClaves": "Plan Austral, Inflación, economía",
        "herramientaBusqueda": "Motores de búsqueda (Google)",
        "segunProcedencia": "Institucional",
        "segunObras": "Bibliográfica",
        "segunForma": "Fraccionada",
        "segunGrado": "Fuente indirecta",
        "anversoTipoFicha": "Ficha de Contenido",
        "anversoAutor": "Mario Rapoport",
        "anversoFechaPublicación": "2000",
        "anversoTitulo": "Historia Política, económica y social de la Argentina",
        "anversoEditorial": "Macchi",
        "anversoLugarEdición": "Buenos Aires. Argentina",
        "anversoOrigenInformación": "Publicación Literaria",
        "reversoTipo": "Resumen",
        "reversoInfo": "Plan Austral: El plan logró cierta estabilidad de precios de inmediato, pero fueron de corto plazo ya que se presentaban problemas estructurales, donde para 1987 la inflación ya superaba el 15% mensual, llegando a una situación crítica del país donde combinaba inflación, recesión, caída de los salarios y desempleo.\nPlan Primavera: corto plazo: inicialmente hubo una desaceleración de la inflación, perdió el control de precios y resultó insostenible. A mediano largo plazo: la inflación se reanudó y el plan no logró estabilizar la economía de forma duradera. En 1989 Argentina sufrió una nueva crisis hiperinflacionaria.",
    },
    {
        "id": "2",
        "fuente": "https://fintualist.com/chile/economia/carlos-menem-y-la-inflacion-en-argentina/",
        "tipoRecurso": "Artículo periodístico",
        "claseFuente": "Secundarias",
        "palabrasClaves": "Menem; Inflación; 1989-1999; Políticas",
        "herramientaBusqueda": "Motores de búsqueda (Google)",
        "segunProcedencia": "personales",
        "segunObras": "Bibliográficas",
        "segunForma": "Fraccionadas",
        "segunGrado": "Indirectas",
        "anversoTipoFicha": "Ficha de documentación",
        "anversoAutor": "Diana Palacios",
        "anversoFechaPublicación": "19 de Febrero del 2021",
        "anversoTitulo": "Carlos Menem y la inflación en Argentina",
        "anversoEditorial": "Fintualist",
        "anversoLugarEdición": "Santiago de Chile, Chile",
        "anversoOrigenInformación": "Sitio web",
        "reversoTipo": "Resumen",
        "reversoInfo": "Carlos Saúl Menem arribó a la presidencia de la República de Argentina en el año 1989 con una inflación anual de 3079% y entregó el mandato con -1,2%. Para disminuir la inflación se adoptaron diferentes políticas que buscaban estabilizar los precios internos y disminuir la emisión de dinero, por esto en 1991 se implementó lo que conocemos por Convertibilidad. Este programa eliminó el austral y dio nacimiento al peso argentino. Las medidas adoptadas lograron reducir notablemente el nivel de precios al punto de que en los últimos años apareció el fenómeno de deflación.",
    },
    {
        "id": "3",
        "fuente": "https://www.infobae.com/economia/2018/07/16/de-peron-a-macri-un-recorrido-por-la-historia-de-la-inflacion-en-argentina/",
        "tipoRecurso": "Artículo periodístico",
        "claseFuente": "Secundarias",
        "palabrasClaves": "De la Rúa; Inflación; Políticas",
        "herramientaBusqueda": "Motores de búsqueda (Google)",
        "segunProcedencia": "personales",
        "segunObras": "Bibliográficas",
        "segunForma": "Fraccionadas",
        "segunGrado": "Indirectas",
        "anversoTipoFicha": "Ficha de documentación",
        "anversoAutor": "Anónimo",
        "anversoFechaPublicación": "16 de Julio de 2018",
        "anversoTitulo": "De Perón a Macri: un recorrido por la historia de la inflación en Argentina.",
        "anversoEditorial": "Infobae",
        "anversoLugarEdición": "Buenos Aires, Argentina",
        "anversoOrigenInformación": "Sitio web",
        "reversoTipo": "Resumen",
        "reversoInfo": "La recesión a fines de 1999 se puede asociar también a un periodo de deflación. Durante el mandato de Fernando de la Rúa, la variación de precios fue negativa, llegando a una tasa anual de -1,1%. La situación llego a su limite en el mes de diciembre de 2001, donde estallo una crisis social que llevo al presidente y su ministro a renunciar",
    },
    {
        "id": "4",
        "fuente": "https://rephip.unr.edu.ar/bitstreams/c44399b1-3a83-4deb-8580-2d3d8d006a0a/download",
        "tipoRecurso": "Publicación Periodística",
        "claseFuente": "Secundarias",
        "palabrasClaves": "crisis de 2001 / discursos políticos",
        "herramientaBusqueda": "Motores de búsqueda (Google)",
        "segunProcedencia": "Institucional",
        "segunObras": "Informativa",
        "segunForma": "Fraccionada ",
        "segunGrado": "Fuente indirecta",
        "anversoTipoFicha": "Ficha de documentación",
        "anversoAutor": "Mariana Cané",
        "anversoFechaPublicación": "Junio 2021",
        "anversoTitulo": "Cinco presidentes: ¿una sola crisis? Articulaciones tópicas y ethos en los discursos presidenciales de fines de 2001 en Argentina",
        "anversoEditorial": "Revista Temas y Debates",
        "anversoLugarEdición": "Buenos Aires. Argentina",
        "anversoOrigenInformación": "Sitio web",
        "reversoTipo": "Resumen",
        "reversoInfo": "El objetivo de este trabajo es recomponer los principales diagnósticos en torno a la crisis delineados en las alocuciones presidenciales de quienes estuvieron al frente del Poder Ejecutivo argentino a fines del 2001, esto es, los dirigentes políticos Fernando De la Rúa, Ramón Puerta, Adolfo Rodríguez Saá, Eduardo Camaño y Eduardo Duhalde. La pregunta que guía la indagación es la siguiente: ¿qué rol jugaron esos diagnósticos y las imágenes de sí proyectadas en sus discursos en las disímiles permanencias en el cargo de cada uno de estos referentes políticos y, particularmente, en los casos de Rodríguez Saá y Duhalde? Para ello, se rastrean en el corpus los principales topoï argumentativos que sustentaron aquellos modos de construir la crisis y los ethos proyectados por cada locutor en su discurso. Nuestra hipótesis de trabajo es que el modo en que Rodríguez Saá y Duhalde diagnosticaron la crisis y construyeron –en sus primeros días de gobierno– su liderazgo contribuyó a delinear sus diferentes performances. En el caso de Rodríguez Saá, favoreció que sus pares le quitaran su apoyo y le valió la salida de la presidencia a una semana de haber asumido. En el de Duhalde, le permitió tejer alianzas con sus pares y construir cierto grado de confianza en la ciudadanía, de modo tal de poder subsanar, al menos en parte, la débil legitimidad de origen de su gestión",
    },
    {
        "id": "5",
        "fuente": "https://cdsa.aacademica.org/000-061/518.pdf",
        "tipoRecurso": "Tesis",
        "claseFuente": "Secundarias",
        "palabrasClaves": "Crisis, acumulación, hegemonía, economía, política",
        "herramientaBusqueda": "Motores de búsqueda (Google)",
        "segunProcedencia": "Institucional",
        "segunObras": "Informativa",
        "segunForma": "Fraccionada",
        "segunGrado": "Fuente indirecta",
        "anversoTipoFicha": "Ficha de documentación",
        "anversoAutor": "Ariel Emilio Fidanza",
        "anversoFechaPublicación": "Año 2015",
        "anversoTitulo": "La salida de la crisis argentina de 2001. Economía y políticas en los gobiernos de Eduardo Duhalde y Néstor Kirchner. XI Jornadas de Sociología",
        "anversoEditorial": "Facultad de Ciencias Sociales, Universidad de Buenos Aires, Buenos Aires.",
        "anversoLugarEdición": "Buenos Aires. Argentina",
        "anversoOrigenInformación": "Sitio web",
        "reversoTipo": "Resumen",
        "reversoInfo": "Como adelanto de la tesis de maestría que aún se encuentra en elaboración, presentamos aquí algunos puntos de debate sobre los aspectos económicos y políticos de la salida de la “crisis de 2001”. Retomando algunos aportes de la bibliografía local, pretendemos dar cuenta de qué significó y cómo fue llevada a cabo la “salida” de la crisis. Entendemos que se trató sobre todo de una crisis de acumulación de capital, que adquirió la forma de las conocidas crisis fiscal, financiera, de recesión, y de una grave crisis política, que terminó con el gobierno constitucional de Fernando de la Rúa en diciembre de 2001. Nuestro objetivo se centra en analizar el gobierno de Eduardo Duhalde (enero de 2002 a mayo de 2003), período que abarca las bases económicas y políticas de una primera y fundamental salida de la crisis, que será completada, en un sentido de continuidad económicas pero de ruptura político-ideológica, por el siguiente gobierno de Néstor Kirchner.",
    },
    {
        "id": "6",
        "fuente": "https://launchpad.ripio.com/blog/historia-de-la-inflacion-en-argentina-cuarta-parte#:~:text=Durante%20los%20cuatro%20a%C3%B1os%20de,y%20del%208.5%25%20en%202007",
        "tipoRecurso": "Publicacion Periodistica",
        "claseFuente": "Secundaria",
        "palabrasClaves": "Inflación. Periodo 2003-2007. Néstor Kirchner",
        "herramientaBusqueda": "Motores de búsqueda (Google)",
        "segunProcedencia": "Institucional",
        "segunObras": "Bibliograficas",
        "segunForma": "Fraccionada",
        "segunGrado": "Fuente indirecta",
        "anversoTipoFicha": "Ficha de documentacion",
        "anversoAutor": "Luis Paz",
        "anversoFechaPublicación": "07 de Julio de 2023",
        "anversoTitulo": "Historia de la inflación en Argentina.",
        "anversoEditorial": "Revista Ripio",
        "anversoLugarEdición": "Buenos Aires, Argentina",
        "anversoOrigenInformación": "Sitio web",
        "reversoTipo": "Síntesis",
        "reversoInfo": "Políticas expansionistas del mercado: aumento del gasto público. Fuerte acción del banco central: compra de monedas extranjeras y adopcion de políticas monetarias más restrictivas. Mejoras sostenidas en los niveles productivos, laborales y de ingresos. Reducción de la tasa de desempleo y pobreza, seguido de expansión industrial. Reestructuración de la deuda externa y saldo de la misma. Cifras del IPC durante su mandato: 4.3%, 9.1%, 10.9% y 8,5% “Fuera de la convertibilidad, fue uno de los periodos de precios mas estables en la historia del país”.",
    },
    {
        "id": "7",
        "fuente": "https://publicaciones.sociales.uba.ar/index.php/hicrhodus/article/view/945",
        "tipoRecurso": "Publicación Académica",
        "claseFuente": "Secundaria",
        "palabrasClaves": "Inflación. Periodo 2007-2015. Cristina Kirchner",
        "herramientaBusqueda": "Motores de búsqueda (Google)",
        "segunProcedencia": "Institucional",
        "segunObras": "Bibliográfica",
        "segunForma": "Fraccionada",
        "segunGrado": "Fuente indirecta",
        "anversoTipoFicha": "Ficha de Contenido",
        "anversoAutor": "Martin Trombetta",
        "anversoFechaPublicación": "2012",
        "anversoTitulo": "Inflación en Argentina y limitaciones del “modelo” kirchnerista",
        "anversoEditorial": "Publicaciones Facultad de Ciencias Sociales UBA",
        "anversoLugarEdición": "Buenos Aires. Argentina",
        "anversoOrigenInformación": "Sitio web",
        "reversoTipo": "Cita textual",
        "reversoInfo": "A comienzos del 2007 el índice de precios al consumidor se disparó rápidamente y comenzó a adoptar valores por encima del 20%, convirtiendo a Argentina en el segundo país con mayor inflación en el mundo. Inicialmente, la respuesta del gobierno a este problema consistió en intentar ocultarlo interviniendo políticamente el Instituto Nacional de Estadísticas y Censos (INDEC), que quedó bajo control de la Secretaría de Comercio del Ministerio de Economía.",
    },
    {
        "id": "8",
        "fuente": "https://www.bbc.com/mundo/noticias-america-latina-50154403",
        "tipoRecurso": "Artículo periodístico",
        "claseFuente": "Secundarias",
        "palabrasClaves": "Macri.FMI.Deficit Fiscal.Cepo.Indec. Inflacion Cero",
        "herramientaBusqueda": "Motores de búsqueda (Google)",
        "segunProcedencia": "Institucional: Institucionales y Documentales",
        "segunObras": "Económicas",
        "segunForma": "Con Imágenes y Numéricas",
        "segunGrado": "Fuente Indirecta",
        "anversoTipoFicha": "Ficha de documentación",
        "anversoAutor": "Cristina J. Orgaz",
        "anversoFechaPublicación": "9 de Diciembre del 2019",
        "anversoTitulo": "Asume Alberto Fernández en Argentina: cómo heredó Macri la economía del país y cómo la deja",
        "anversoEditorial": "BBC news mundo",
        "anversoLugarEdición": "Buenos aires, Argentina",
        "anversoOrigenInformación": "Sitio web",
        "reversoTipo": "Resumen",
        "reversoInfo": "Cuando en 2015, Mauricio Macri ganó las elecciones presidenciales en Argentina, los organismos internacionales y los mercados financieros consideraron al candidato de centro derecha algo así como el hombre destinado a meter al país en el camino de la disciplina fiscal. Cuando llegó al poder, el presidente de Argentina, Mauricio Macri, prometió reducir la inflación y llevar la pobreza a 'cero'. Pero ambos capítulos de la economía aumentaron durante su gobierno",
    },
    {
        "id": "9",
        "fuente": "https://www.lanacion.com.ar/politica/guerra-contra-la-inflacion-alberto-fernandez-anuncia-el-paquete-de-medidas-economicas-nid18032022/?gad_source=1&gclid=EAIaIQobChMI2run9b7MiAMVy1VIAB323CojEAAYAyAAEgIS0_D_BwE",
        "tipoRecurso": "Artículo periodístico",
        "claseFuente": "Secundarias",
        "palabrasClaves": "Inflación, Gasto público, Déficit fiscal, Reservas.",
        "herramientaBusqueda": "Motores de búsqueda (Google)",
        "segunProcedencia": "Institucional",
        "segunObras": "Económicas",
        "segunForma": "Con imágenes, numéricas",
        "segunGrado": "Fuente indirecta",
        "anversoTipoFicha": "Ficha de documentación",
        "anversoAutor": "Santiago Dapelo",
        "anversoFechaPublicación": "19 de marzo del 2022",
        "anversoTitulo": "Sin anuncios concretos, Alberto Fernández dilató las medidas contra la inflación y confirma un aumento de las retenciones",
        "anversoEditorial": "La Nación",
        "anversoLugarEdición": "Buenos Aires- Argentina",
        "anversoOrigenInformación": "Sitio web",
        "reversoTipo": "Resumen",
        "reversoInfo": "Dos grandes problemas marcarían también el gobierno de Fernández: la escasez de dólares y la renegociación del acuerdo con el FMI, que asciende la deuda a unos US $45.000 millones. El acuerdo con el FMI nos permite comenzar a ordenar las variables macroeconómicas centrales en la lucha contra la inflación que es, como lo decimos siempre, un fenómeno multicausal. Para atacarla debemos acumular reservas, mejorar el crédito público, desacoplar los precios internos de los internacionales, trabajar sobre las políticas de ingresos y precios al mismo tiempo y tomar una batería de medidas en las que múltiples actores son imprescindibles. Las políticas más representativas del gobierno fueron: \n1. Aumento del Gasto Público: Se incrementó el gasto en salud y asistencia social para enfrentar la pandemia de COVID-19. \n2.. Impuestos: Se introdujo el 'Aporte Solidario y Extraordinario' para las grandes fortunas, también se realizaron ajustes en el sistema impositivo para aumentar la recaudación. \n3. Control de la inflación: regulación de precios y tarifas, con resultados limitados debido a la persistencia de altos índices inflacionarios. \n4. Controles de Cambio: Se mantuvieron estrictos controles sobre la compra de divisas y la fuga de capitales. \n5. Política de Tasas de Interés: El Banco Central ajustó las tasas de interés para controlar la inflación y estimular la economía",
    },
    {
        "id": "10",
        "fuente": "https://www.youtube.com/watch?v=6VPsoaniNxI",
        "tipoRecurso": "Audiovisual",
        "claseFuente": "Secundaria",
        "palabrasClaves": "Inflación. Políticas Monetarias. Gobierno. Recesión",
        "herramientaBusqueda": "Motores de búsqueda (Youtube)",
        "segunProcedencia": "Institucional",
        "segunObras": "Legislativas",
        "segunForma": "Con imágenes y numéricas",
        "segunGrado": "Fuente indirecta",
        "anversoTipoFicha": "Ficha de documentación",
        "anversoAutor": "La Nación",
        "anversoFechaPublicación": "12 de diciembre 2023",
        "anversoTitulo": "Anuncios de Luis Caputo",
        "anversoLugarEdición": "Buenos Aires, Argentina",
        "anversoOrigenInformación": "Sitio web (Youtube)",
        "reversoTipo": "Resumen",
        "reversoInfo": "Esto va a redundar en una reducción de más del 50% del gasto de la función pública. Reducción al mínimo de las transferencias a las provincias. El Estado nacional no va a licitar obra pública y cancelará las que se haya licitado y no se haya ejecutado. Reducción de los subsidios a energía y transporte. “Se pagan con inflación”, indicó. Mantener los planes potenciar trabajo y mantener las políticas sociales sin intermediarios. Vamos a sincerar el tipo de cambio oficial 800 pesos. Esto va a estar acompañado por un aumento provisorio del impuesto país a las importaciones y a las retenciones de las exportaciones no agropecuarias. Finalizada esta emergencia Vamos a avanzar en la eliminación de todos los derechos de importación, que entorpecen el desarrollo argentino",
    },
]


def home_view(request):
    return render(request, "home.html", {"fichas": presidentes})


def theory_view(request):
    return render(request, "theory.html")


def cards_view(request):

    ficha_id = request.GET.get("ficha")
    ficha_seleccionada = None

    if ficha_id: 
        ficha_seleccionada = next((ficha for ficha in fichas if ficha["id"] == ficha_id), None)    

    return render(request, "cards.html", {"ficha": ficha_seleccionada, "presidentes": presidentes})


def sobre_nosotros_view(request):
    
    ctx = [
        {
            "id": "1",
            "carrera": "Contador Público",
            "apellido": "Mansilla",
            "nombre": "Iris",
            "img": "MansillaIris",
            "gmail": "mansillairis612@gmail.com",
            "instagram": "iris_jmansilla"
        },
        {
            "id": "2",
            "carrera": "Contador Público",
            "apellido": "Martínez Borda",
            "nombre": "Victoria Alejandra",
            "img": "MartínezBordaVictoriaAlejandra",
            "gmail": "vicky080500@hotmail.con",
            "instagram": "victoriamborda"
        },
        {
            "id": "3",
            "carrera": "Contador Público",
            "apellido": "Oviedo",
            "nombre": "Sergio",
            "img": "OviedoSergio",
            "gmail": "sergiodav_@hotmail.com",
            "instagram": "serg_oviedo"
        },
        {
            "id": "4",
            "carrera": "Contador Público",
            "apellido": "Piaggio",
            "nombre": "María Belén",
            "img": "PiaggioMaríaBelén",
            "gmail": "Belenpiaggio7@gmail.com",
            "instagram": "belenpiaggio"
        },
        {
            "id": "5",
            "carrera": "Licenciatura en Economía",
            "apellido": "Piedrabuena",
            "nombre": "Martina Lilian",
            "img": "PiedrabuenaMartinaLilian3",
            "gmail": "piedrabuenam21@gmail.com",
            "instagram": "mrtnp_"
        },
        {
            "id": "6",
            "carrera": "Contador Público",
            "apellido": "Rea",
            "nombre": "Eduardo Gabriel",
            "img": "ReaEduardoGabriel",
            "gmail": "Eduardogabrielrea@gmail.com",
            "instagram": "Gabrielrea28"
        },
    ]

    miembro_id = request.GET.get("member")
    miembro_selected = ctx[0]

    if miembro_id: 
        miembro_selected = next((miembro for miembro in ctx if miembro["id"] == miembro_id), ctx[0])    

    return render(request, "sobre_nosotros.html", {'integrantes': ctx, "miembro": miembro_selected})