# Disk Scheduling Algorithms

Este proyecto implementa y compara tres algoritmos de planificación de disco:

- FCFS
- SCAN
- C-SCAN

El programa simula un disco con 5000 cilindros, numerados desde 0 hasta 4999. Además, genera 1000 solicitudes aleatorias de cilindros y calcula el movimiento total del cabezal para cada algoritmo.

El objetivo principal es analizar cómo se comporta cada algoritmo y comparar la cantidad total de movimiento del cabezal del disco.

---

## Requisitos

Para ejecutar el proyecto se necesita tener instalado:

- Python
- Matplotlib

Para instalar `matplotlib`, se puede usar el siguiente comando:

```bash
pip install matplotlib
```

Si el comando anterior no funciona, también se puede usar:

```bash
python -m pip install matplotlib
```

---

## Archivo principal

El archivo principal del programa se llama:

```bash
cilindros.py
```

Este archivo contiene la implementación de los algoritmos FCFS, SCAN y C-SCAN, además de la generación de gráficas.

---

## Ejecución del programa

El programa recibe por línea de comandos la posición inicial del cabezal del disco.

La estructura general del comando es:

```bash
python cilindros.py <posicionInicial>
```

La posición inicial debe ser un número entre 0 y 4999.

---

## Ejemplo utilizado

Para este trabajo se usó el siguiente ejemplo:

```bash
python cilindros.py 1023
```

En este caso, el cabezal inicia en el cilindro 1023.

Al ejecutar el programa, se generan 1000 solicitudes aleatorias y se calcula el movimiento total del cabezal para cada algoritmo.

Un ejemplo de salida fue:

```text
Resultados de planificacion de disco
-----------------------------------
Posicion inicial del cabezal: 1023
Cantidad de solicitudes generadas: 1000

Movimiento total FCFS: 1735457 cilindros
Movimiento total SCAN: 8972 cilindros
Movimiento total C-SCAN: 9990 cilindros
```

Los resultados pueden cambiar en cada ejecución porque las solicitudes se generan de forma aleatoria.

---

## Imágenes generadas

Además de mostrar los resultados en consola, el programa genera imágenes con las gráficas de cada algoritmo.

Las imágenes generadas para el ejemplo usado fueron:

```text
movimiento_cabezal_FCFS.png
movimiento_cabezal_SCAN.png
movimiento_cabezal_C-SCAN.png
comparacion_rendimiento.png
```

Estas imágenes fueron generadas usando el comando:

```bash
python cilindros.py 1023
```

Las gráficas permiten observar el comportamiento del cabezal del disco durante la ejecución de cada algoritmo.

---

## Cómo generar tus propios ejemplos

Para generar tus propios ejemplos, solo debes cambiar el número de la posición inicial del cabezal.

Por ejemplo:

```bash
python cilindros.py 500
```

```bash
python cilindros.py 2150
```

```bash
python cilindros.py 4000
```

Cada vez que se ejecuta el programa:

1. Se generan 1000 solicitudes aleatorias.
2. Se calcula el movimiento total usando FCFS.
3. Se calcula el movimiento total usando SCAN.
4. Se calcula el movimiento total usando C-SCAN.
5. Se generan las gráficas correspondientes.

La posición inicial siempre debe estar en el rango:

```text
0 a 4999
```

Si se ingresa una posición fuera de ese rango, el programa muestra un mensaje de error.

---

## Algoritmos implementados

### FCFS

FCFS significa First Come First Served.

Este algoritmo atiende las solicitudes en el mismo orden en que llegan.

Es un algoritmo sencillo, pero puede generar mucho movimiento del cabezal, ya que no tiene en cuenta la posición de las solicitudes en el disco.

### SCAN

SCAN también es conocido como el algoritmo del elevador.

Este algoritmo mueve el cabezal en una dirección, atiende las solicitudes que encuentra en el camino, llega hasta el final del disco y luego cambia de dirección.

Esto permite reducir el movimiento total del cabezal en comparación con FCFS.

### C-SCAN

C-SCAN es una variante de SCAN.

La diferencia principal es que C-SCAN siempre se mueve en la misma dirección. Cuando llega al final del disco, vuelve al inicio y continúa atendiendo solicitudes en la misma dirección.

Este comportamiento permite que el servicio sea más uniforme y predecible.

---

## Visualización de datos

El programa genera dos tipos de visualizaciones:

### Movimiento del cabezal

Se genera una gráfica para cada algoritmo:

- Movimiento del cabezal en FCFS
- Movimiento del cabezal en SCAN
- Movimiento del cabezal en C-SCAN

Estas gráficas muestran el orden en que se atienden las solicitudes y el cilindro visitado por el cabezal.

### Comparación de rendimiento

También se genera una gráfica de barras que compara el movimiento total del cabezal en los tres algoritmos.

Esta comparación permite observar cuál algoritmo tuvo menor movimiento total en la simulación.

---

## Comparación del ejemplo usado

En el ejemplo ejecutado con:

```bash
python cilindros.py 1023
```

se obtuvo que FCFS tuvo un movimiento mucho mayor que SCAN y C-SCAN.

Esto ocurre porque FCFS atiende las solicitudes en orden aleatorio, mientras que SCAN y C-SCAN organizan mejor el recorrido del cabezal.

En la simulación realizada, SCAN tuvo el menor movimiento total, mientras que C-SCAN tuvo un movimiento ligeramente mayor debido al salto desde el final del disco hasta el inicio.

---

## Conclusión

La simulación permite observar que FCFS no es el algoritmo más eficiente cuando las solicitudes están distribuidas aleatoriamente, ya que el cabezal se mueve constantemente entre cilindros alejados.

SCAN y C-SCAN reducen considerablemente el movimiento total del cabezal al atender las solicitudes de forma más ordenada.

SCAN puede presentar menor movimiento total en algunos casos, mientras que C-SCAN ofrece una atención más uniforme porque siempre se mueve en la misma dirección.
