# Configuración Base de Datos

## Crear y ejecutar el contenedor OracleDB

```bash
docker run -d --name oracle -p 1521:1521 -e ORACLE_PASSWORD=oracle -v data:/opt/oracle/oradata gvenzl/oracle-xe:21-slim
```

## Acceder al contenedor

```bash
$ docker exec -it oracle bash
```

## Conectarse a OracleDB

```bash
sqlplus
```

Usa usuario `system` y contraseña `oracle`

## Crear usuario y conceder permisos

```sql
--Crear un usuario
Create user SEMINARIO_DEV identified by "53m1N4R10.";
-- Conceder permisos de conexión y más
grant connect, resource, DBA to SEMINARIO_DEV;
```

## Cambiar de usuario

Salir del usuario `system` e ingresar al usuario recien creado

```sql
exit
```

<!-- ##  Ejecutar scripts de inserción

```sql
start creacion_p.sql;
start insersion_p.sql;
```

Este paso a paso anterior solo se debe realizar **una vez**, después de la descarga y ejecución del contenedor y después de ejecutar el algoritmo de creación de tablas e inserción de registros.  -->

## Encender el contenedor si está apagado

Al apagar y encender la maquina, el contenedor estara "apagado", para "encenderlo" se ejecuta el siguiente comando:

```bash
docker start oracle
```

