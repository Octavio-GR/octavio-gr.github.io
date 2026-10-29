# Proyecto Toroide — Matriz maestra de trazabilidad

- **Estado:** Borrador para revisión; no integrado en `main`
- **Fecha de elaboración:** 2026-10-28
- **Repositorio de referencia:** `Octavio-GR/octavio-gr.github.io`
- **Línea base documental inspeccionada:** `main`
- **Horizonte propuesto:** 14 días desde la aprobación del plan

**Objetivo:** mantener decisiones, pendientes, evidencia y criterios de cierre fuera de la memoria conversacional.

## 1. Objetivo del producto

Toroide tiene tres objetivos compatibles, pero no intercambiables:

1. **Empleabilidad:** demostrar capacidades reales mediante proyectos y evidencias inspeccionables para reclutadores.
2. **Laboratorio técnico:** documentar arquitectura, decisiones, experimentos, límites y resultados reproducibles.
3. **Monetización:** evaluar vías sostenibles de ingresos sin degradar la experiencia, la integridad técnica ni la calidad del contenido.

La identidad visual distintiva —basada en geometría y un sistema visual coherente— es un trabajo central, no un adorno que se añade al final. Antes de cerrar el logo deben revisarse las ideas, bocetos y compromisos históricos disponibles. El archivo `toroide/LOGO.md` actualmente define requisitos de uso, pero no acredita por sí solo que exista un logo final aprobado.

## 2. Reglas de trazabilidad

- No marcar una tarea como completada solo porque exista una página o un documento.
- Separar **implementación**, **evidencia**, **verificación** y **publicación**.
- Cada claim público debe tener evidencia adecuada y alcance explícito.
- No convertir ideas históricas en tareas activas sin clasificarlas.
- Cada pendiente activo debe incluir responsable/decisión requerida, siguiente acción y criterio de cierre.
- Mantener el alcance de cambios pequeños; no hacer limpieza masiva ni normalizar archivos ajenos al cambio.
- `main` es la línea base publicada. Los cambios locales no inspeccionados quedan fuera de este documento hasta reconciliarlos.
- Los seis PDF de CV locales no forman parte de este alcance y no deben añadirse a commits de mantenimiento sin una decisión explícita.
- No publicar cambios en `main` sin revisar el diff, validar enlaces y contenido, y recibir autorización de publicación.

## 3. Estado de arquitectura y fases

| Área | Estado documental observado | Lo que sí puede afirmarse | Pendiente real |
|---|---|---|---|
| Fases 1–3 | Marcadas completas en `toroide/ROADMAP.md` | La documentación declara fundamentos, identidad y arquitectura completados | Confirmar que las declaraciones siguen alineadas con el producto actual, sin reabrir fases ya estables por defecto |
| Fase 4 — Perception | Funcional; pulido final pendiente | El propio roadmap mantiene pendiente el pulido final | Definir y ejecutar una pasada visual integral después de establecer el sistema visual |
| Fase 5 — Materialization | Operativamente madura | Milestones 002 y 003 se declaran completados | Cerrar discrepancias entre claims, contenido, pruebas y experiencia visible |
| Fase 6 — Validation | Completada con limitaciones en informes previos | Hay resultados históricos de validación local documentados | No repetir toda la batería sin cambios; ejecutar la validación final una vez después de corregir |
| Fase 7 — QDEE | Completada con limitaciones | `docs/AUDITS/F7-QDEE-01.md` documenta alcance y límites | Mantener límites explícitos y ejecutar solo las comprobaciones pendientes que afecten el cierre |
| M7 visual | Revisión estática completada con limitaciones | `docs/AUDITS/M7-VISUAL-01.md` no establece un defecto visual funcional confirmado | Inspección visual real en navegador y alineación de claims, cuando se trabaje la identidad visual |

## 4. Matriz de exhibits y claims

La etiqueta `Verified` en `docs/EXHIBITS.md` identifica el estado registrado del exhibit; **no equivale a certificar todos sus claims**. `docs/PROOF.md` y los informes de auditoría conservan limitaciones que deben prevalecer para formular afirmaciones públicas.

| Exhibit | Estado registrado | Evidencia / límite actual | Condición de cierre |
|---|---|---|---|
| EX-001 — Toroide Construction | `Verified` en el registro | README describe arquitectura observable, estructura y Git como evidencia; no es una evaluación externa de competencia | Revisar página y README juntos; elegir 1–3 decisiones concretas con evidencia localizable y explicación reproducible |
| EX-002 — Zero JavaScript Runtime | `Verified` en el registro; claim limitado | La afirmación defendible es que el contenido, layout y navegación centrales no requieren JavaScript de primera parte. Existe observación histórica de una solicitud a Cloudflare Insights; no afirmar cero JS de red | Alinear titular, README y página; conservar alcance preciso. Captura de red solo si se desea sostener una afirmación de runtime |
| EX-003 — Progressive Disclosure | `Verified` en el registro | `docs/PROOF.md` indica que la capacidad necesita verificación independiente | Comprobar que la interfaz revela detalle por capas de manera real y que enlaces/rutas funcionan; documentar observación concreta |
| EX-004 — Context Stack | `Verified` en el registro | El informe M7 detecta claims amplios sobre registrar “cada” paso y reconstruir el estado “exacto”; no está demostrada la exhaustividad del historial | Limitar el claim a los registros realmente existentes y probar un caso de reconstrucción desde documentos y Git |
| EX-005 — Accessibility | `Verified` en el registro | Hay estructura semántica y un cálculo de contraste documentado, pero no existe certificación WCAG 2.1 AA completa | Verificar teclado, foco visible, zoom/reflow, estructura, contraste y estados relevantes. No declarar conformidad integral sin evaluación documentada |

### Regla de cierre de los exhibits

Cada exhibit debe incluir:
1. pregunta o problema concreto;
2. descripción que no exceda la implementación;
3. evidencia identificable;
4. método de verificación que otra persona pueda repetir;
5. limitaciones explícitas;
6. enlaces locales válidos;
7. consistencia entre HTML, README y registros.

La finalidad de los cinco exhibits es ayudar a los reclutadores a inspeccionar capacidades reales. No deben usarse como sustituto de experiencia que no esté demostrada ni como prueba automática de dominio profesional.

## 5. Identidad, logo y sistema visual

| Elemento | Estado observado | Siguiente paso | Criterio de cierre |
|---|---|---|---|
| Logo (DF-009) | `toroide/LOGO.md` contiene requisitos de uso; no acredita una versión final | Recuperar y revisar bocetos, imágenes y acuerdos históricos antes de diseñar una propuesta nueva | Una propuesta elegida y aprobada por el usuario; legible en monocromo, favicon 16×16, avatar y soportes definidos |
| Sistema visual | `toroide/DESIGN_SYSTEM.md` declara “En construcción” | Definir geometría, tipografía, escala, color, espaciado, composición, estados y reglas de uso | Documento operativo con tokens/reglas coherentes aplicados al sitio y a los cinco exhibits |
| Octágono | `docs/TECH_DEBT.md` registra contraste diagonal como deuda observada | Resolver junto con la dirección visual; evitar parche aislado antes de fijar identidad | Contraste perceptible a escala normal, verificado en navegador y sin degradar legibilidad |
| Hero / CTA | TD-004 aparece diferido | Revisar jerarquía cuando la identidad y el objetivo dual estén definidos | Acción principal y secundaria identificables, con texto alineado a empleabilidad/laboratorio |
| Presentación profesional | `docs/IDENTITY.md` presenta Toroide como observatorio, no portafolio convencional | Conciliar esa narrativa con el objetivo explícito de empleabilidad, laboratorio y monetización | Mensaje inicial comprensible para reclutadores sin borrar el carácter de laboratorio técnico |

**Nota histórica del logo:** el usuario recuerda un compromiso conversacional de preparar una sorpresa visual. En los documentos de `main` inspeccionados no aparece un artefacto de logo final ni evidencia suficiente para afirmar que esa imagen esté terminada o disponible. Antes de reemplazar la idea, revisar conversaciones/adjuntos históricos accesibles. No inventar ni reconstruir como hecho un boceto que no se haya encontrado.

## 6. Contenido, blog y monetización

| Área | Estado | Siguiente acción | Criterio de cierre |
|---|---|---|---|
| Google AdSense (DF-010) | **Aviso confirmado por el usuario:** “Detectamos algunos incumplimientos de política”. Identifica “Anuncios publicados por Google en pantallas sin contenido de publicadores” y “Contenido de bajo valor”. Google enumera pantallas sin contenido o con contenido de bajo valor, pantallas en construcción y pantallas de navegación/alerta; además pide información/herramientas/servicios auténticos y de alta calidad, contenido mantenido e interés genuino de usuarios. | Auditar cada URL donde se muestran o podrían mostrarse anuncios; identificar páginas vacías, en construcción, de navegación o con poco valor editorial; revisar originalidad, profundidad, utilidad, mantenimiento y experiencia. Separar páginas de laboratorio/documentación que sí aportan valor de páginas que solo funcionan como índice o navegación. Consultar las políticas oficiales enlazadas en la notificación antes de decidir qué retirar, ampliar o excluir de anuncios. | Lista de URLs clasificadas con evidencia, correcciones priorizadas y revisión contra la política citada. No prometer aprobación ni asumir que todo el sitio infringe; el aviso confirma el tipo de política detectado, no identifica aquí cada URL causante. |
| `redrogue.blogspot.com` | Migración recordada como pendiente; no se ha inventariado el contenido en esta revisión | Inventariar publicaciones, autoría, imágenes, enlaces, fechas y contenido que merece conservarse. Distinguir migración, archivo y descarte | Decisión por publicación/categoría, destino definido, atribución/licencias revisadas y enlaces de origen/destino documentados |
| Storytelling personal | Idea histórica en `DO_NOT_FORGET`; compatible con el objetivo de empleabilidad, pero no desarrollada en esta matriz | Preparar narrativa profesional basada en hechos, decisiones y artefactos demostrables | Sección breve que conecte motivación, capacidades y evidencias sin exagerar credenciales |
| Monetización futura | Idea histórica; ahora confirmada como objetivo del usuario | Evaluar AdSense y alternativas solo después de entender el problema de contenido; preservar UX y credibilidad | Hipótesis de monetización, requisitos, riesgos y decisión documentados; no incorporar anuncios por defecto |
| Easter egg clandestino (DF-008) | El usuario quiere un descubrimiento discreto, con referencia a un sitio de contenido adulto | Redefinirlo como una experiencia no sexual, apta para todo público y sin dirigir a pornografía. Acordar el concepto antes de implementarlo | Easter egg accesible, no engañoso en seguridad, no expone datos y no enlaza a contenido pornográfico |

El aviso aportado confirma que AdSense señaló dos categorías de política: anuncios en pantallas sin contenido de publicadores y contenido de bajo valor. No identifica en el texto compartido qué URLs concretas originaron el hallazgo ni demuestra que todas las páginas del sitio sean incumplidoras. La causa por URL debe establecerse mediante inventario e inspección del sitio. No incluir credenciales ni datos privados de la cuenta en este documento.

## 7. Ideas históricas de `DO_NOT_FORGET`

Los estados siguientes son una **clasificación de trabajo**, no una afirmación de que exista una decisión histórica definitiva. Los elementos ambiguos quedan marcados para consulta puntual.

| Idea | Estado propuesto | Base de la clasificación | Pregunta/acción |
|---|---|---|---|
| Octagon animation | Aplazada | La identidad geométrica aún debe cerrarse; animar antes puede generar retrabajo | Revisarla después del sistema visual |
| Papa Pascual eggs | Aplazada — decisión confirmada por el usuario | El significado y alcance no están descritos en los documentos inspeccionados | No implementar durante el cierre de 14 días; reabrir solo si el usuario lo prioriza y define el concepto |
| Rubik cube concept | Descartada — decisión confirmada por el usuario | No existe especificación recuperada en los documentos inspeccionados | No dedicar trabajo ni reintroducirla sin una nueva decisión explícita del usuario |
| Toroid mathematics | Activa (propuesta) | Encaja con el objetivo confirmado de laboratorio técnico | Definir el fenómeno/contenido exacto y una demostración verificable |
| Blog migration | Activa | El usuario volvió a confirmar la intención de recuperar `redrogue.blogspot.com` | Inventario y decisión editorial por contenido |
| Personal storytelling | Activa (propuesta) | Encaja con empleabilidad; falta acordar el contenido autobiográfico | Borrador basado en hechos y revisión del usuario |
| Future monetization | Activa | El usuario confirmó monetización y reportó un bloqueo de AdSense | Diagnosticar el aviso antes de elegir solución |

## 8. Seguridad, accesibilidad y calidad

| Pendiente | Evidencia actual | Política de cierre |
|---|---|---|
| WCAG 2.1 AA | `docs/PROOF.md` la marca Pending; F7 indica que no se hizo auditoría completa | Evaluación documentada por páginas/estados; no afirmar conformidad completa antes de tener resultados |
| Cabeceras HTTP | F7-SEC-01 las marca no verificadas | Capturar respuestas HTTP reales de páginas representativas y registrar fecha/URL |
| Runtime / terceros | EX-002 tiene límites expresos; existe observación histórica de una solicitud de tercero | No confundir inspección estática con captura de red |
| CSS duplicado | El validador reportó warnings, no defectos confirmados | No refactorizar globalmente sin defecto concreto y revisión del cascade |
| Validación local | `scripts/validate.ps1` tiene resultados históricos PASS documentados | Ejecutar una vez al final de los cambios relevantes; no repetir inspecciones sin causa |
| Backups locales | El usuario informó que 92 `.bak` fueron movidos al graveyard fuera del repo y se añadió `*.bak` a `.gitignore`; estos cambios locales no están verificados en esta revisión | Proteger los cambios locales y comprobar su estado antes de cualquier integración. No borrar el graveyard |
| CV en PDF | Se reportaron seis PDF locales sin publicar | Fuera del alcance de mantenimiento; no incluirlos sin decisión explícita |

## 9. Plan de cierre acelerado — 14 días

El día 1 comienza cuando el usuario apruebe este alcance. La secuencia prioriza decisiones que evitan retrabajo; no promete que todas las metas amplias (migración completa o monetización efectiva) se resuelvan en dos semanas.

### Días 1–2 — Congelar línea base y recuperar contexto
- Proteger el estado local y separar cambios ajenos al cierre.
- Recuperar bocetos/ideas históricos del logo.
- El aviso de AdSense ya fue aportado: registrar el diagnóstico de política y revisar las páginas de destino de los anuncios frente al contenido realmente disponible.
- Inventariar `redrogue.blogspot.com` sin migrar todavía.
- Aplicar las decisiones confirmadas: Papa Pascual eggs queda aplazada; el concepto del cubo Rubik queda descartado.

**Salida:** inventario de decisiones, contenido histórico y riesgos, sin cambios de interfaz todavía.

### Días 3–5 — Cerrar dirección visual
- Presentar una o más propuestas de logo basadas en los bocetos recuperados y en `LOGO.md`.
- Definir sistema visual mínimo operativo: geometría, tipografía, color, espaciado, composición y estados.
- Aplicar primero a la página principal y verificar en escritorio/móvil.

**Salida:** dirección visual aprobada, logo y sistema visual coherentes; no comenzar animaciones secundarias antes.

### Días 6–8 — Alinear y cerrar los cinco exhibits
- Comparar cada HTML con su README y con `docs/EXHIBITS.md` / `docs/PROOF.md`.
- Corregir solo claims excesivos, inconsistencias o defectos observados.
- Preparar evidencia reproducible para EX-001–EX-005.
- Verificar navegación y presentación visual real.

**Salida:** los cinco exhibits alineados y honestos; ningún claim amplio sin prueba.

### Días 9–10 — Narrativa, contenido y blog
- Alinear el mensaje principal con empleabilidad + laboratorio.
- Crear inventario de entradas de Red Rogue y clasificarlas para migrar, archivar o descartar.
- Diseñar el Easter egg como descubrimiento no sexual, apto para todo público.

**Salida:** narrativa profesional revisable y plan de migración editorial, sin copiar contenido indiscriminadamente.

### Días 11–12 — Monetización y comprobaciones acotadas
- Auditar el aviso confirmado de AdSense: pantallas sin contenido de publicadores y contenido de bajo valor.
- Construir un inventario de URLs donde se muestran o se planean anuncios; clasificar páginas con contenido sustancial, páginas de navegación/índice y páginas en construcción.
- Priorizar contenido original útil, páginas completas y experiencia de usuario antes de solicitar otra revisión; evaluar excluir anuncios de páginas que no sean aptas según la política vigente.
- Capturar cabeceras HTTP de producción y hacer la comprobación de accesibilidad acordada que quepa en el alcance.
- Registrar límites no resueltos, sin presentarlos como fallos confirmados.

**Salida:** diagnóstico de monetización y evidencia técnica final con limitaciones declaradas.

### Días 13–14 — Validación, revisión y liberación
- Ejecutar una sola batería final de validación relevante.
- Revisar `git diff --check`, enlaces, HTML/CSS afectados y coherencia documental.
- Revisar el diff completo, excluyendo PDF y artefactos ajenos.
- Solicitar autorización explícita antes de commit/push/merge.
- Tras la publicación autorizada, verificar el deployment de GitHub Pages.

**Salida:** paquete de cierre revisado, con decisiones pendientes separadas y evidencia de publicación si se autoriza.

## 10. Definición de terminado

El cierre acelerado se considera listo para revisión cuando:
- los cinco exhibits tienen claims proporcionales a la evidencia;
- la dirección visual y el logo tienen una decisión explícita del usuario;
- el sistema visual mínimo está documentado y aplicado de forma consistente;
- las ideas históricas tienen estado o pregunta concreta;
- AdSense tiene diagnóstico basado en el mensaje real, no suposiciones;
- la migración de Red Rogue tiene inventario y decisión editorial;
- las limitaciones de accesibilidad, runtime y cabeceras están declaradas;
- la validación final pasa dentro del alcance;
- el diff excluye cambios no autorizados y los seis PDF;
- no se publica nada sin revisión y autorización.

## 11. Fuentes inspeccionadas

- `toroide/ROADMAP.md`
- `toroide/LOGO.md`
- `toroide/DESIGN_SYSTEM.md`
- `toroide/DO_NOT_FORGET.md`
- Notificación de política de Google AdSense transcrita por el usuario el 2026-10-28 (evidencia aportada en conversación; no se ha verificado la cuenta directamente).
- `docs/IDENTITY.md`
- `docs/TECH_DEBT.md`
- `docs/PROOF.md`
- `docs/EXHIBITS.md`
- `docs/MILESTONES.md`
- `docs/INDEX.md`
- `docs/AUDITS/F7-QDEE-01.md`
- `docs/AUDITS/M7-VISUAL-01.md`
- `exhibits/001-toroide-construction/README.md`
- `exhibits/002-zero-javascript-runtime/README.md`
- `exhibits/003-progressive-disclosure/README.md`
- `exhibits/004-context-stack/README.md`
- `exhibits/005-accessibility/README.md`

## 12. Control de cambios

Este documento es una propuesta para revisión. Su preparación no modifica `main`, no aprueba los cambios locales existentes y no autoriza publicación. Toda integración requiere revisar el alcance y el diff final.
