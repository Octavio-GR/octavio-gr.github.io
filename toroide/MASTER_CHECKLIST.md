# TOROIDE — CHECKLIST MAESTRO DE CONTINUIDAD Y CIERRE

**Última reconciliación:** 2026-11-01
**Repositorio:** `Octavio-GR/octavio-gr.github.io`
**Rama de referencia:** `main`
**Línea base:** `d153eee` — `docs: reconcile roadmap and verification statuses`

## Propósito y reglas operativas

Mantener una única lista rectora de tareas, decisiones, evidencia y criterios de cierre del Proyecto Toroide.

- El estado documentado no sustituye la comprobación de la implementación.
- No marcar una tarea como completada únicamente porque se haya escrito o actualizado su documentación.
- No inferir detalles que no estén respaldados por archivos, evidencia o decisiones explícitas del usuario.
- No duplicar tareas ya registradas en `toroide/DO_NOT_FORGET.md` o `docs/TECH_DEBT.md`; esta lista las consolida y enlaza con sus fuentes.
- No eliminar respaldos locales sin comprobar primero su función y destino.
- Mantener fuera de los commits de mantenimiento los seis PDF locales de CV hasta decidir su publicación.
- Cualquier futura publicación requiere autorización explícita. La autorización de esta intervención cubre la actualización acotada de este archivo.

**Estados:** `Completado`, `En curso`, `Pendiente`, `Diferido`, `Por decidir`, `Descartado`. Una tarea diferida no es un fallo; una tarea documentada no equivale a una tarea ejecutada.

---

## 1. Mantenimiento y línea base del repositorio

### Confirmado

- [x] Revisar el alcance del commit `df9f3b3`, que actualizó `.gitignore`, `docs/EVIDENCE.md` y `toroide/AUDITS.md` para documentar la higiene de respaldos.
- [x] Confirmar que `git ls-files '*.bak'` no devuelve respaldos rastreados.
- [x] Confirmar la regla `*.bak` de `.gitignore` mediante `git check-ignore`.
- [x] Confirmar que el inventario local detecta cinco archivos `.bak` ignorados. No eliminarlos como parte de esta reconciliación.
- [x] Mantener los seis PDF nuevos fuera de los commits de mantenimiento.
- [x] Revisar la conciliación documental de roadmap, hitos y trazabilidad publicada en `d153eee`.

### Pendiente

- [ ] Confirmar que el directorio externo `graveyard/repo-backups-20261028-204023` y su manifiesto CSV existen y que el manifiesto corresponde a los 92 respaldos archivados originalmente.
- [ ] Determinar si los cinco respaldos locales detectados son copias posteriores o forman parte de otra operación. Conservarlos hasta tener una decisión segura.
- [ ] Resolver de forma mínima la diferencia de finales de línea de `toroide/AUDITS.md` (`i/lf w/mixed`). Inspeccionar el diff y corregir solo si se confirma una discrepancia accidental; no normalizar el archivo completo por defecto.
- [ ] Ejecutar una validación consolidada del alcance exacto de esta intervención.
- [ ] Verificar el despliegue y la versión publicada después del push; no darlo por hecho a partir de un commit exitoso.

## 2. Documentación central: estado de reconciliación

### Revisado en el alcance actual

- [x] `toroide/ROADMAP.md`, `docs/MILESTONES.md` y `toroide/TRACEABILITY.md`: se ajustaron las afirmaciones generales de verificación en `d153eee`; las limitaciones de cada exhibit siguen siendo autoritativas.
- [x] `docs/EVIDENCE.md`: distingue afirmaciones, observaciones, artefactos y mediciones; el estado de despliegue de la limpieza de respaldos sigue pendiente.
- [x] `docs/PROOF.md`: conserva estados parciales o conceptuales cuando no hay evidencia suficiente para una conclusión más fuerte.
- [x] `docs/EXHIBITS.md`: EX-001 a EX-005 mantienen estados distintos; no inferir conformidad WCAG 2.1 AA completa ni ausencia de toda actividad JavaScript de terceros.
- [x] `docs/OBSERVATIONS.md`: se mantiene como descripción de identidad observable, no como backlog operativo.
- [x] `toroide/DECISIONS.md`: ADR-001 a ADR-006 están marcadas como aceptadas. No reabrirlas sin evidencia concreta de conflicto.
- [x] `docs/TECH_DEBT.md`: TD-001 observado; TD-002 a TD-004 diferidos; TD-005 y TD-006 completados según el registro.

### Pendiente; revisar solo cuando corresponda a una tarea concreta

- [ ] `toroide/AUDITS.md`: cerrar la comprobación dirigida de finales de línea y conciliar el resumen con informes individuales solo donde haya una discrepancia concreta.
- [ ] `docs/INDEX.md` y `docs/README.md`: verificar rutas y límites entre documentación pública, exhibits y documentación interna.
- [ ] `docs/FOUNDATIONS.md`, `docs/CORE_LOOP.md` y `toroide/DESIGN_SYSTEM.md`: comprobar coherencia de principios si se modifica la arquitectura o el sistema visual.
- [ ] `docs/IDENTITY.md` y `docs/IDENTITY_OCTAVIO.md`: distinguir identidad del proyecto y presentación profesional cuando se trabaje la narrativa de empleabilidad.
- [ ] Mantener `toroide/DO_NOT_FORGET.md` como registro de continuidad e historia de decisiones; no copiarlo entero a esta lista.

## 3. Backlog histórico consolidado

Los identificadores PT son referencias operativas creadas para esta lista, no identificadores históricos originales. Las entradas DF y TD conservan la fuente de procedencia. Los estados propuestos se identifican como tales cuando no existe una decisión confirmada.

### PT-001 — Recuperar y aprobar la identidad visual y el logo

- **Estado:** Pendiente.
- **Fuente:** `toroide/DO_NOT_FORGET.md` (DF-009) y `toroide/LOGO.md`.
- **Acción:** revisar las conversaciones, bocetos y adjuntos históricos accesibles antes de reemplazar la idea por una propuesta nueva.
- **Criterio de cierre:** registrar qué referencias se recuperaron y obtener aprobación explícita del artefacto final, o documentar una decisión de aplazamiento.

### PT-002 — Refinamiento visual del octágono

- **Estado:** Observado; prioridad baja.
- **Fuente:** `docs/TECH_DEBT.md` (TD-001).
- **Acción:** evaluar la pérdida de contraste de los bordes diagonales a distancia normal de visualización.
- **Criterio de cierre:** comparación visual reproducible y decisión documentada de corregir o conservar el estado actual.

### PT-003 — Animación del octágono

- **Estado:** Diferido.
- **Fuente:** `toroide/DO_NOT_FORGET.md` (DF-001).
- **Acción:** reconsiderar después de cerrar la geometría, el logo y el sistema visual.
- **Criterio de cierre:** decisión explícita de mantenerla diferida o implementarla; si se implementa, respetar movimiento reducido y no bloquear contenido.

### PT-004 — Matemáticas del toroide

- **Estado:** Activo propuesto; alcance por definir.
- **Fuente:** `toroide/DO_NOT_FORGET.md` (DF-004).
- **Acción:** elegir el concepto matemático que se quiere explicar y la demostración o derivación verificable que lo sustenta.
- **Criterio de cierre:** explicación precisa, fuente o derivación identificable y visualización fiel si se necesita, con límites documentados.

### PT-005 — Inventario y posible migración del blog histórico

- **Estado:** Activo.
- **Fuente:** `toroide/DO_NOT_FORGET.md` (DF-005); origen indicado: `redrogue.blogspot.com`.
- **Acción:** inventariar entradas, imágenes, enlaces, fechas, autoría y dependencias. No importar todo en bloque.
- **Criterio de cierre:** decisión por contenido (migrar, archivar o descartar), atribución y derechos revisados, y destino registrado.

### PT-006 — Narrativa profesional basada en evidencia

- **Estado:** Activo propuesto.
- **Fuente:** `toroide/DO_NOT_FORGET.md` (DF-006).
- **Acción:** reunir experiencias, decisiones, aprendizajes y artefactos demostrables que apoyen el objetivo de empleabilidad.
- **Criterio de cierre:** texto aprobado por el usuario, concreto y verificable, sin inflar credenciales ni resultados.

### PT-007 — Estrategia de monetización y diagnóstico de AdSense

- **Estado:** Activo; diagnóstico incompleto.
- **Fuente:** `toroide/DO_NOT_FORGET.md` (DF-007 y DF-010).
- **Evidencia disponible:** el usuario informó avisos sobre anuncios en pantallas sin contenido de editor y contenido de bajo valor.
- **No demostrado:** las URL exactas afectadas, el alcance del problema y qué corrección resolvería la revisión.
- **Acción:** inventariar las páginas que contienen anuncios o son candidatas a mostrarlos; clasificar contenido sustancial, índices/navegación, páginas en construcción y posibles páginas de bajo valor; contrastar los hallazgos con la política vigente.
- **Criterio de cierre:** mapa de URL con hallazgos verificables, correcciones prioritarias y revisión documentada antes de que el usuario decida solicitar una nueva evaluación. No prometer aprobación.

### PT-008 — Easter egg discreto

- **Estado:** Por decidir.
- **Fuente:** `toroide/DO_NOT_FORGET.md` (DF-008).
- **Acción:** decidir si se desea la experiencia y definir pista y recompensa aptas para todo público. No crear flujos hacia pornografía ni exponer datos personales.
- **Criterio de cierre:** concepto aprobado antes de implementarse; si se aprueba, debe ser accesible por teclado, no engañoso respecto a seguridad y respetuoso de la privacidad.

### PT-009 — «Papa Pascual eggs»

- **Estado:** Aplazado por decisión confirmada el 2026-10-28.
- **Fuente:** `toroide/DO_NOT_FORGET.md` (DF-002).
- **Acción:** ninguna durante el cierre acelerado. Reabrir solo si el usuario lo prioriza y define el concepto.
- **Restricción:** no inferir significado, diseño, contenido ni alcance.

### PT-010 — Concepto del cubo Rubik

- **Estado:** Descartado por decisión confirmada el 2026-10-28.
- **Fuente:** `toroide/DO_NOT_FORGET.md` (DF-003).
- **Acción:** ninguna.
- **Restricción:** no reintroducir sin una nueva decisión explícita del usuario.

### PT-011 — Optimización de recursos y pipeline

- **Estado:** Diferido; prioridad media.
- **Fuente:** `docs/TECH_DEBT.md` (TD-002).
- **Acción:** no añadir minificación, optimización SVG ni compresión automatizada hasta que exista una necesidad justificada y un pipeline apropiado.
- **Criterio de cierre:** decisión revisada ante una necesidad medible; no crear infraestructura por anticipado.

### PT-012 — Validación continua (CI)

- **Estado:** Diferido; prioridad media.
- **Fuente:** `docs/TECH_DEBT.md` (TD-003).
- **Acción:** mantener las validaciones locales existentes. Reevaluar CI si aparece una necesidad concreta de integración, compilación o despliegue automatizado.
- **Criterio de cierre:** decisión documentada basada en necesidad operativa, no en la mera disponibilidad de GitHub Actions.

### PT-013 — Jerarquía de CTA del Hero

- **Estado:** Diferido; prioridad baja.
- **Fuente:** `docs/TECH_DEBT.md` (TD-004).
- **Acción:** revisar cuando el contenido permita evaluar la importancia relativa de las acciones.
- **Criterio de cierre:** jerarquía justificada por contenido y evaluada en la interfaz; no reabrir solo por preferencia estética.

### PT-014 — Estandarización de directorios de exhibits

- **Estado:** Completado según el registro.
- **Fuente:** `docs/TECH_DEBT.md` (TD-005).
- **Acción:** ninguna, salvo que evidencia nueva revele una regresión.

### PT-015 — Consistencia de nombres del repositorio

- **Estado:** Completado según el registro.
- **Fuente:** `docs/TECH_DEBT.md` (TD-006).
- **Acción:** ninguna, salvo que evidencia nueva revele una regresión.

## 4. Portafolio profesional y CV

- [ ] Revisar el contenido y metadatos de los seis PDF locales antes de cualquier publicación.
- [ ] Definir qué especialidades profesionales se presentarán públicamente.
- [ ] Decidir si los CV se publicarán, se entregarán bajo solicitud o permanecerán locales.
- [ ] Revisar privacidad de datos personales y laborales.
- [ ] Definir enlaces, etiquetas y ubicación de acceso desde el sitio, si se aprueba la publicación.
- [ ] Confirmar que la narrativa profesional complementa, pero no sustituye, la evidencia técnica.
- **Restricción vigente:** los seis PDF no forman parte de esta intervención ni de ningún commit de mantenimiento hasta tomar la decisión de publicación.

## 5. Orden recomendado de ejecución

1. [ ] Cerrar la validación dirigida de mantenimiento y la cuestión de los finales de línea, sin limpieza destructiva.
2. [ ] Recuperar referencias históricas del logo y decidir identidad visual; después reevaluar la animación y el octágono.
3. [ ] Inventariar el blog histórico antes de seleccionar contenido para migración.
4. [ ] Definir el alcance de la demostración matemática del toroide.
5. [ ] Construir la narrativa profesional a partir de artefactos verificables y decidir el destino de los CV.
6. [ ] Diagnosticar AdSense mediante inventario de URL y políticas vigentes, sin presuponer la causa.
7. [ ] Resolver explícitamente el diseño del easter egg antes de implementarlo.
8. [ ] Mantener las ideas aplazadas y descartadas cerradas hasta que cambien las condiciones o el usuario decida reabrirlas.

## 6. Criterios de cierre global

- [ ] No hay estados contradictorios entre roadmap, hitos, auditorías, deuda técnica, registro de decisiones y evidencia.
- [ ] Cada elemento marcado como completado tiene una fuente o prueba identificable.
- [ ] Cada pendiente importante tiene fuente, acción siguiente y criterio de cierre.
- [ ] Las decisiones diferidas y descartadas no se presentan como trabajo activo.
- [ ] Las limitaciones conocidas no se expresan como capacidades verificadas.
- [ ] Los enlaces y las rutas documentales relevantes apuntan a archivos existentes.
- [ ] La validación consolidada no deja errores sin clasificar.
- [ ] El commit contiene únicamente los archivos aprobados y excluye cambios locales ajenos y los seis PDF.
- [ ] El despliegue se comprueba después del push; el push por sí solo no acredita el despliegue.

## Regla para evitar ciclos de revisión

1. Recopilar la evidencia disponible una sola vez.
2. Analizarla como conjunto y consolidar hallazgos.
3. Corregir los hallazgos aceptados en una intervención coherente.
4. Ejecutar una validación final dirigida a los criterios de aceptación.
5. Reabrir una comprobación solo si falla una prueba, cambia el alcance o aparece evidencia contradictoria.

**No volver a solicitar contenido ya compartido salvo que exista una discrepancia concreta y explicada.**
**No marcar una tarea como completada solo porque esté documentada.**
**No publicar cambios futuros sin autorización explícita.**
