# TOROIDE — CHECKLIST MAESTRO DE CONTINUIDAD Y CIERRE DOCUMENTAL

**Propósito:** Mantener trazabilidad entre las decisiones, la implementación, la evidencia, el estado real del proyecto y los pendientes.

**Regla operativa:** Los archivos locales constituyen la fuente de trabajo vigente. No solicitar nuevamente su contenido si ya fue proporcionado en la conversación y no existe evidencia concreta de una discrepancia.

## 1. Registro de cambios y mantenimiento actual

- [ ] Revisar conjuntamente el diff de `.gitignore`, `docs/EVIDENCE.md` y `toroide/AUDITS.md`.
- [ ] Resolver la diferencia aparente de finales de línea en `toroide/AUDITS.md` sin normalizar innecesariamente el archivo completo.
- [ ] Confirmar que el registro de limpieza de los 92 archivos `.bak` coincide con la operación realizada.
- [ ] Confirmar que el manifiesto y las copias de respaldo permanecen fuera del repositorio.
- [ ] Ejecutar una única validación consolidada de los cambios y del estado de Git.
- [ ] Excluir los seis PDF nuevos de cualquier commit de mantenimiento hasta definir su función dentro del portafolio.
- [ ] Preparar el commit únicamente con los archivos expresamente aprobados.
- [ ] Obtener autorización antes de ejecutar commit y push.
- [ ] Verificar el despliegue y la versión publicada después del push.

## 2. Conciliación de la documentación central

- [ ] `toroide/ROADMAP.md`: contrastar las fases y los hitos con el trabajo efectivamente realizado.
- [ ] `docs/MILESTONES.md`: comprobar que los estados «Completed» tienen evidencia suficiente.
- [ ] `toroide/AUDITS.md`: conciliar el resumen de auditorías con los informes individuales.
- [ ] `docs/EVIDENCE.md`: separar observaciones, artefactos, mediciones, afirmaciones y evidencia pendiente.
- [ ] `docs/OBSERVATIONS.md`: conservar su función de documentar la identidad observable del sitio.
- [ ] `toroide/DECISIONS.md`: comprobar que las decisiones relevantes estén documentadas y sean rastreables.
- [ ] `docs/TECH_DEBT.md`: identificar deuda vigente, diferida y resuelta.
- [ ] `docs/EXHIBITS.md`: conciliar el registro EX-001 a EX-005 con su estado real y sus limitaciones.
- [ ] `docs/INDEX.md` y `docs/README.md`: comprobar que las rutas y las categorías documentales correspondan a archivos existentes.
- [ ] `docs/FOUNDATIONS.md`, `docs/CORE_LOOP.md` y `toroide/DESIGN_SYSTEM.md`: conservar coherencia entre fundamentos, proceso y criterios visuales.
- [ ] `docs/IDENTITY.md` y `docs/IDENTITY_OCTAVIO.md`: distinguir la identidad conceptual del proyecto de la presentación profesional de su autor.
- [ ] `toroide/DO_NOT_FORGET.md`: convertir los pendientes recuperados en tareas explícitas, sin duplicar listas ya mantenidas en otros documentos.

## 3. Conciliación del historial del proyecto

- [ ] Recuperar las tareas acordadas que no llegaron a implementarse.
- [ ] Recuperar las ideas aplazadas, incluidas las de identidad visual y logo.
- [ ] Identificar decisiones tomadas que todavía no tienen implementación.
- [ ] Identificar implementaciones que todavía carecen de documentación o evidencia.
- [ ] Identificar afirmaciones de finalización que requieren una salvedad.
- [ ] Distinguir lo completado, lo parcialmente completado, lo pendiente, lo diferido y lo rechazado.
- [ ] Vincular cada pendiente importante con un archivo, una acción y un criterio de cierre.
- [ ] Evitar crear tareas duplicadas o reabrir decisiones ya resueltas sin evidencia nueva.

## 4. Portafolio profesional y CV

- [ ] Revisar los seis PDF incorporados localmente.
- [ ] Definir qué especialidades profesionales se presentarán públicamente.
- [ ] Decidir si los CV se publicarán, se ofrecerán bajo solicitud o permanecerán locales.
- [ ] Revisar la privacidad de los datos personales y laborales antes de publicar.
- [ ] Definir enlaces, etiquetas y ubicación de acceso desde el sitio.
- [ ] Verificar que la presentación profesional complemente, sin sustituir, la evidencia técnica de Toroide.

## 5. Criterios de cierre

- [ ] No existen estados contradictorios entre roadmap, hitos, auditorías y evidencia.
- [ ] Cada hito declarado como completado tiene respaldo identificable.
- [ ] Los pendientes históricos recuperados están registrados o tienen una decisión explícita.
- [ ] Las limitaciones conocidas no se presentan como capacidades verificadas.
- [ ] La documentación y los enlaces relevantes son coherentes.
- [ ] La validación consolidada no reporta errores pendientes sin clasificar.
- [ ] El alcance del commit está revisado y aprobado.
- [ ] El estado publicado se comprueba después del despliegue.

## Regla para evitar ciclos de revisión

1. Recopilar la evidencia disponible una sola vez.
2. Analizar el conjunto y producir una lista consolidada de hallazgos.
3. Corregir los hallazgos aceptados en una sola intervención coherente.
4. Ejecutar una validación final dirigida a los criterios de aceptación.
5. Reabrir una comprobación únicamente si falla una prueba, cambia el alcance o aparece evidencia contradictoria.

**No volver a solicitar el contenido de un archivo local ya compartido salvo que exista una razón concreta y explicada.**

**No considerar terminado un pendiente por haberlo documentado: el estado debe reflejar lo realmente ejecutado.**

**No publicar cambios sin autorización explícita.**
