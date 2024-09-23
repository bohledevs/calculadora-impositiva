# Proyecto: Calculadora Impositiva


## Objetivo 
- El objetivo de este módulo de software es asistir a un usuario vendedor con los impuestos aplicables a cada una de sus transacciones.

## Alcance
- Incorpora impuestos nacionales (__IVA__, Ganancias *de ahora en más __IIGG__*), y provinciales (Ingresos Brutos, *de ahora en más __IIBB__*) 
- La exactitud contable no está asegurada. Es posible que una o más reglas de negocio de la calculadora estén sujetas a cambios, en su configuración actual o futura.


## Diseño y Arquitectura

### Casos de uso

- Especificación

![Casos de uso](./diagramas/casos-de-uso.png)

- Código PUML
```plantuml
@startuml
left to right direction
actor "Vendedor" as vd <<Humano>>
rectangle "Calculadora Impositiva" {
  usecase "Calcular impuestos nacionales" as UC1
  usecase "Calcular impuestos provinciales" as UC2
  usecase "Evaluar condición fiscal" as UC3
  UC3 .up.> UC1 : <<extends>>
  UC3 .up.> UC2 : <<extends>>
}
vd -down-> UC1
vd -down-> UC2
@enduml
```

### Reglas de negocio

#### Impuestos nacionales
- Los impuestos nacionales se aplican en base a la condición fiscal (*__CF__*) ingresada por pantalla. Pueden tomar tres valores:
1. IVA Exento: para usuarios excluídos de impuestos nacionales, por ejemplo entes estatales o empresas del estado.
2. Responsable Inscripto: Para personas inscriptas en el régimen IVA, por ejemplo, monotributistas.
3. Consumidor Final: Para personas que no están inscriptas en IVA, por ejemplo, vendedores casuales.

- Diagrama de Actividad:

![Impuestos nacionales](./diagramas/impuestos-nacionales.png)

- Codigo PUML

```plantuml
@startuml

start

:Ingresar datos 
-monto 
-condicion fiscal (cf);

if (cf == 'IVA Exento'?) then (yes)
  :iva = 0%
  ganancias = 0%;
else (no)
  if (cf == 'Responsable Inscripto'?) then (yes)
   :iva = 10.5%
   ganancias = 0.5%;
  else (no)
   if (cf == 'Consumidor Final'?) then (yes)
    :iva = 21.0%
    ganancias = 2%;
   else (no)
    :Error, condicion fiscal\nno existente;
   endif
  endif
endif 

:impuesto_iva = monto*iva/100
impuesto_ganancias = monto*ganancias/100;

:mostrar_montos(impuesto_iva, impuesto_ganancias);

stop

@enduml
```

#### Impuestos provinciales
- Los impuestos provinciales se aplican en base al régimen IIBB (*__reg__*) ingresado por pantalla. Pueden tomar tres valores:
1. No Inscripto: El usuario no está inscripto en ningún régimen. Aplica la alícuota más alta.
2. Local: El usuario está inscripto sólo en su provincia, aplica una alícuota intermedia.
3. Multilateral: E
