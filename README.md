# Introducción a la programación probabilística

Se utiliza en Machine Learning, Medicina, Investigación...

P(H|E) = P(H and E) / P(E) = P(H) P(H|E) / P(H)P(H|E) + P(¬H) P(H|¬E)

P(H) = Prior
p(H|E) = posterior

La probabilidad se puede entender como la propocion de que un evento ocurra dentro de la proporcion mas grande todos los eventos que pueden ocurrir.

"Cum Hoc Ergo Propter Hoc : Despues de esto, eso, entonces a consecuencia de eso, esto"

Pensar fuera de la caja para pensar en todas las probabilidades posibles que puedan explicar un evento

Prejuicio en el muestreo: Generalizar los datos y obtener conclusiones en base de una muestra no representativa.

Falacia del francotirador: No se toma aleatoriedad en consideracion, enfocar similitudes e ignorar las diferencias, fallar al tener una hipotesis antes de tener datos nos da alto riesgo de caer en la falacia.

Porcentajes confusos: Cuando no se sabe la cuenta total del cual se obtiene un porcentaje tenemos el riesgo de concluir falsos resultados, es importante saber el contexto.

Falacia regresion: Cuando algo fluctua naturalemtne y se aplican medidas correctivas se puede creer que existe un vinculo de casualidad en lugar de una regresion a la media, ejemplo el rendimiento de un atleta, racha de juegos ganados.

Machine Learning: Es la capacidad de las computadoras sin ser explicitamente programadas, no hay inteligencia autonoma sino son algoritmos matematicas muy complejos que realizan calculos para simular aprendizaje a como lo hace el ser humano.

Se utiliza machine learning cuando: 
    - Programar un algoritmo es imposible
    - El problema es muy complejo o no se conocen los algoritmos para resolverlo
    - Ayuda a los humanos a entender patrones (data mining)

    Aprendizaje supervisado vs no supervisado vs semisupervisado

    Supervisado
    - Se estudia y organiza la información que entra para detectar patrones y con esto construir modelos.

    Semi-supervisado
    - Se tiende a organizar la información inicial y  luego se le da una etiqueta a algunos ejemplos, despues la maquina por medio de patrones o esquemas prestablecidos por la misma se da etiquetas a nuevos datos.

Feature Vectors

    - Se utilizan para representar caracteristicas simbolicaso numericas llamadas features
    - Permiten analizar un objeto desde una perspectiva matematica
    - Los algoritmos de machine learning tipicamente requieren representaciones numericas para poder ejecutar el computo
    - Uno de los features vectors mas conocidos es la representacion del color a traves de RGB

    Problemas relacionados: 
    - Procesamiento de imagenes
    - Reconocimiento de voz
    - Spam

Metricas de distancia

    - Muchos de los algoritmos de machine learning pueden clasificarse como algoritmos de optimizacion

    - Distancia de Manhattan: Mide la distancia de un punto a otro punto siguiendo una ruta posible

Introduccion al agrupamiento (clustering):
    
    - Es un proceso mediante el cual se agrupan objetos similares en clusters que los identifican

    - Se clasifica como aprendizaje no supervisado ya que no requiere la utilizacion de etiquetas

    - Permite entender la estructura de los datos y la similitud entre los mismos

    - Es utilizado en motores de recomendacion, analisis de redes, sociales, analisis de riesgo crediticio, clasificacion de genes, riesgos medicos, etc.

Agrupamiento jerarquico: 

    - Es un algoritmo que agrupa objetos similares en grupos llamados clusters

    - El algoritmo trata cada objeto como un cluster individual despues realiza los siguientes pasos de manera recursiva

    - El enfoque es deterministico a menos que cambiemos la metrica siempre obtendremos el mismo dendograma

    - La complejidad algoritmica es del orden O(n^2), lo cual hace que sea muy lento a medida que aumenta la dimensionalidad de los datos, por eso se tiende a usar otros metodos como Kmeans

    - No se usa en caso de que la cantidad de datos sea muy grande ya que puede afectar el aspecto visual y puede ser confuso


Introducción a la Clasificación 

    - Es el proceso mediante cual se predice la clase de cierto dato
    - Es un tipo de aprendizaje supervisado ya que para que funcione, se
    necesitan etiquetas con los datos (labels)
    - Se utiliza en muchos dominios, incluyendo la medicina, aprobación crediticia, reconocimiento de imágenes, vehículos autónomos, entre otros.
    - Sigue dos pasos: aprendizaje (cración del modelo y clasificación)

K Nearest Neighbours:

    - Parte de un conjunto de datos que ya tenemos clasificado
    - Trata de encontrar los "vecinos mas cercanos"
    - K se refiere a la cantidad de vecinos que se usaran para clasificar un ejemplo que no ha sido clasificado
    - Es sencillo de implementar y tiene aplicaciones en diversos campos
    - Es muy costoso computacionalmente y no sirve para procesar datos de alta dimensionalidad

