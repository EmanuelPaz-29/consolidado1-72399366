# Consolidado 1 - Construcción de Software

**Nombre completo:** Emanuel Paz Mottoccanchi
**Código de alumno:** 72399366
**Curso:** Construcción de Software (ASUC00947) - VII Ciclo
**Universidad:** Universidad Continental - Ingeniería de Sistemas e Informática
**Periodo:** 2026-20

## Descripción del proyecto

Repositorio de la Práctica Calificada - Consolidado 1 (Semanas 5, 6 y 7: POO, Git y Gitflow). Contiene tres ejercicios en Python con programación orientada a objetos, desarrollados con el flujo Gitflow (ramas main, develop, feature y hotfix) y commits con formato Conventional Commits.

## Archivos del repositorio

- `planeta.py`: clase Planeta con atributos, cálculo de densidad media, clasificación de planeta exterior o interior (umbral de 5.2 UA) y método __str__.
- `automovil.py`: clase Automovil con atributos privados y propiedades (@property) con validación de año, nivel de combustible y velocidad máxima, además del método tiempo_llegada.
- `cuentas.py`: jerarquía de cuentas bancarias con herencia: CuentaBancaria (clase base), CuentaAhorros (cálculo de interés) y CuentaCorriente (límite de sobregiro).

## Ramas

- `main`: versión estable.
- `develop`: integración de las funcionalidades.
- `feature/clase-planeta`, `feature/clase-automovil`, `feature/cuenta-bancaria`: una rama por ejercicio.
- `hotfix/validar-monto`: corrección urgente creada desde main y fusionada en main y develop.