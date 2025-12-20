# SRH - SISTEMA DE RESERVAS DE HOTELES BACKEND - FASTAPI

Backend del Sistema de Reservas de Hoteles (SRH)

UNIVERSIDAD POLITÉCNICA SALESIANA - UPS


Materia: Ingeniería de Software  

Tarea: T02.03

Grupo: B

Estudiante: Andrea Murillo Medina

Fecha: 22/12/2025

Docente: Darío Huilcapi


## Gestión del Proyecto

El repositorio del proyecto fue creado en GitHub para el control de versiones
y seguimiento del desarrollo. Las tareas del proyecto fueron definidas y
asignadas a la única integrante activa del grupo Andrea Murillo, quien realizó de manera
individual todas las actividades de análisis, diseño, implementación y
documentación del backend de la aplicación.

## Asignación de Tareas

- Backend y framework FastAPI: Andrea Murillo  
- Gestión de clientes, habitaciones y reservas: Andrea Murillo  
- Documentación Swagger: Andrea Murillo  
- Control de versiones y repositorio GitHub: Andrea Murillo


## Cumplimiento de la SRS y la DDS

El desarrollo del backend se realizó tomando como base los requerimientos
funcionales definidos en la Tarea 02.01 (SRS) y las descripciones de diseño
planteadas en la Tarea 02.02 (DDS). Para esta implementación se desarrollaron
los módulos núcleo del sistema: Clientes, Habitaciones y Reservas, los cuales
representan el flujo principal del sistema de reservas hoteleras.


## Backend y Framework

El backend del proyecto corresponde a una API REST desarrollada para el Sistema
de Reservas de Hoteles. Para la implementación del backend se utilizó el
framework FastAPI, el cual permitió la creación de servicios REST eficientes y
la documentación automática de los endpoints mediante Swagger.


## Documentación de Servicios

Los servicios REST desarrollados se encuentran documentados mediante Swagger,
accesible a través del endpoint /docs, lo que permite visualizar y probar los
endpoints del backend de manera interactiva.

## Arquitectura del Sistema

El backend fue desarrollado siguiendo un esquema de arquitectura por capas,
separando modelos, esquemas (schemas) y controladores (routers), equivalente al
modelo/repositorio/controlador/servicio definido en la consigna, lo que permite
un código modular, ordenado y mantenible.

## Ejecución y Visualización

Para ejecutar el backend del SRH, se debe levantar el servidor con el siguiente comando:

```bash
uvicorn app.main:app --reload

Una vez iniciado el servidor, el sistema puede visualizarse en:

Página principal del backend:
http://127.0.0.1:8000

Documentación de los servicios (Swagger):
http://127.0.0.1:8000/docs