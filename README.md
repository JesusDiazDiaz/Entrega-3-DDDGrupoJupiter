# Entrega 4 - Diseño de la experimentacion y POC de Servicios
GRUPO JUPITER

Repositorio con código base para el uso de un sistema usando el patrón CQRS y usando eventos de dominio 
Estamos simulado un atributo de calidad de escalabilidad con un escenario de actualizacion de caracteristicas, segun se describe en grafica anexa:
![](files/atributo-calidad.png)
![diagrama CyC solucion](https://github.com/JesusDiazDiaz/Entrega-3-DDDGrupoJupiter/assets/111446386/769e4823-2b8c-4253-863d-36d03015ef42)


## Estructura del proyecto

Este repositorio sigue la siguiente estructura, hemos incorporado 4 microservicios: 1. Auditoria (enriquecimiento de informacion por auditores), 2. Compañias (son las vistas de los clientes), 3. Pipeline (detecta la completitud de informacion que recoge propiedades), 4. Propiedades (hace la busqueda e ingesta de datos de las propiedades en fuentes externas):


- **api**: En este módulo tenemos el API de `enrequecimiento.py` el cual cuenta con dos endpoints: `/audit` y `audit`, los cuales por detrás de escenas usan un patrón CQRS como la base de su comunicación.
- **modules/../enrequecimiento/application**: Este módulo ahora considera los sub-módulos: `queries` y `commands`. En dichos directorios se desacopló las diferentes operaciones lectura y escritura.
- **modules/../enrequecimiento/domain**: 
- **modules/../enrequecimiento/infraestructure**: Este archivo cuenta con toda la lógica en términos de infrastructura para consumir los eventos y comandos
- **modulos/../validacion/application**:  
- **modulos/../validacion/domain**: 
- **seedwork/application/**: 
- **seedwork/domain/**: 
- **seedwork/infraestructure/**: 
- **seedwork/presentation/**: 

## Propiedades de los Alpes
### Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.
Debe tener el daemon de Docker corriendo previamente, y luego ejecuta docker-compose para que suba todo.


```bash
docker-compose build
```

```bash
docker-compose up
```

En el siguiente enlace se encuentra la documentación de los servicios expuestos por el microservicio auditoria:
[Documentacion postman](https://documenter.getpostman.com/view/1827448/2sA2rDy1na)
