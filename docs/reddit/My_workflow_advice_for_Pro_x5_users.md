#My workflow advice for Pro x5 users [Visit](https://www.reddit.com/r/codex/comments/1wf46gp/my_workflow_advice_for_pro_x5_users/)
### **Subreddit:** [r/codex](https://www.reddit.com/r/codex)
### **Author:** [kyrax80](https://www.reddit.com/user/kyrax80/)
### **Vote:** 26
---
I see many users, inclusing x20 users complaining about usage, yesterday I was almost whole day using Codex, in parallel tasks and just used 25%. This is how I do it, it's pretty simple and I hope it can help someone:
- Don't use same conversation for planning and for implementing. Use one for each and when you think it's getting too long just start a new one.
- Use Astra low for planning complex tasks and Sol med-high for not complex tasks. Use Luna xHigh for implementing. I'd dare to say Luna xHigh has implemented 95% everything properly with no mistakes. In my [AGENTS.md](http://AGENTS.md) I have stated that for planning Codex should tell what code to implement, modify or delete for medium/difficult tasks.
- Don't plan for very simple tasks, just use Luna low-med. Let's say to change a component's color, size, etc. For UI stuff what I do is to use ChatGPT on web and ask it to create a design that I like, then ask it for the HTML and CSS and handle it to Codex. Then ask Codex to adapt it to your project. I use Angular for front-end for example, handle it the code ChatGPT gave me and tell Codex to use that exact code but to adapt it to my project, create reusable components and stuff like that.
- When planning, give as detailed as possible instructions, not just "Create an UI for this".
Today I've been working with Codex for 1h, made a plan with Astra low, 1 implementation with it and some small changes without a plan, just used 1% so far or not even that (was at 75% when started and at 74% now)
Hope this can help some of you, give it a try, specially if you're on x5. Of course this is on a normal project, not to reverse engineer a whole backend with fast mode as I saw in a post not so long ago.
For Plus users I'd suggest to use Terra high/ Sol low to plan and Luna to implement but I don't really know what would work for them and x20 users maybe can use Astra med to implement easy tasks and high for comples ones and then Terra to implement. I have 2 banked resets aside of last reset so I'm trying different combinations and this one looks the best so far for me.
Cheers!
---
## Comments 26

- by [unknown](#) **&#x21C5; 14**
  <br/> The more thinking you give the AI with ambiguous terms, the more usage it will eat.

"Make a UI", this is so open ended it will take ages and spend loads of usage

"Make a UI based on X, with the features we discussed" it still has to trawl through the repo and map everything based on X

"Here's an image of the UI made roughly with boxes in powerpoint, each one has a code on name, usage, scroll, button, sub-menu, hook these up to the corresponding names in the repo in this specific section". It knows exactly where the code is to map the buttons, and you've given it zero thinking and told it exactly what to map to what. As a Plus user, I made an entire Unity UI setup using just 20% usage via this method. That's 4% on a 5x pro account. Give it LESS thinking. It may seem obvious to a human who has used UI's for years, AI hasn't, and it has thousands to pick from in it's training set. High thinking models WILL iterate through those and validate them, eating up vast swathes of usage just to pick a UI, before the build.

Remove the thinking parts - far less usage gets eaten. Coding is cheap. I can code myself so I know how to prompt, but my entire repo in a game of over 5000 lines at this point is about 10% of Plus account usage, at most. Take it's thinking away and give it exact instructions and it just become a dev with few mistakes at cheap rates. The issue is vibe coders giving it ambiguous plain english prompts to build an entire software suite and wondering why they can't do that for $200, LOL.

- by [unknown](#) **&#x21C5; 2**
  <br/> Yes, I forgot to mention that too. For UI stuff what I do is to use ChatGPT on web and ask it to create a design that I like, then ask it for the HTML and CSS and handle it to Codex. I'll add this to the post, thanks!

- by [unknown](#) **&#x21C5; 1**
  <br/> Nice, just give me another Reset to try out (and fail miserably)

- by [unknown](#) **&#x21C5; 7**
  <br/> Your also forgetting the point that chat, yes chat not work but chat on 5x gives you 20 pro latest model sessions and 200 on pro 20x.

Your literally using chat with your linked GitHub repo to implement and using 0 codex credits.

People literally have 2x the amount of capability respectively to 5/20x accounts and people aren't aware of how to use the tooling properly.

- by [unknown](#) **&#x21C5; 1**
  <br/> When does the 200 on pro 20x get reset?

- by [unknown](#) **&#x21C5; 2**
  <br/> Weekly, same as codex. Or every time you use a banked reset, or a global reset.

- by [unknown](#) **&#x21C5; 4**
  <br/> "Don't use same conversation for planning and for implementing. "

I assume you use ChatGPT for the conversation, right?

- by [unknown](#) **&#x21C5; 2**
  <br/> No, I used Codex. Is it better to use ChatGPT and how can I do it? With Work? It doesn't consume tokens?

- by [unknown](#) **&#x21C5; 3**
  <br/> Do not use work as that is tied to codex usage, use chat instead. You can add GitHub to chat so codex and chat can both interact with the repo so you just do all the planning in chat as that is separate usage from codex. Then just implement that plan in codex.

Like you could have chat write handoff planning MDs in the repo and you implement in codex saying follow XYZ MD.

I have this setup for chat, codex, and Hermes, all in the same workspace to work on stuff for my portfolio site. Every agent signs off a handoff doc so the next agent knows what happened last, etc.

- by [unknown](#) **&#x21C5; 1**
  <br/> Chat + Github is a very good approach. I guess chat can't read PC's folders so Github isn't needed? Thanks!

- by [unknown](#) **&#x21C5; 2**
  <br/> Chat is dumb af. Use work/codex. Usage is irrelevant because planning hardly uses any.

- by [unknown](#) **&#x21C5; 1**
  <br/> I think you mean GitHub *is needed* with chat, right? Because yeah i don't think chat can access local folders. Work can I believe but that uses codex usage which is what you're trying to avoid.

- by [unknown](#) **&#x21C5; 1**
  <br/> you do it on chat, then copy paste or attach the chat to a codex session for context

- by [unknown](#) **&#x21C5; 1**
  <br/> Holy token burn… yes Chat GPT projects are where you plan (for free) it keeps all planning in separate conversations but all in the same context window of the project + you can add sources.

- by [unknown](#) **&#x21C5; 3**
  <br/> What used to be the recommended workflow for Plus users is now recommended for 5x, lmao.

- by [unknown](#) **&#x21C5; 1**
  <br/> Sad but true lol

- by [unknown](#) **&#x21C5; 2**
  <br/> This is an awesome suggestion. Thanks!!

- by [unknown](#) **&#x21C5; 2**
  <br/> Use Luna xHigh for implementing.


    No thanks, I want my code to actually work. I use Astra low for planning, Sol low for implementation.

Plus user fwiw. Limits are not too bad if you avoid cache misses. And that includes not using subagents because their behavior causes cache misses.

- by [unknown](#) **&#x21C5; 1**
  <br/> Well, if that works for you, it's valid. Luna xhigh works perfectly for me so far and if it doesn't all I have to do is change to a better model. I think Sol for implementing is an overkill tho

- by [unknown](#) **&#x21C5; 1**
  <br/> It's still a work in progress and I'm sure will always be as I've got some absurd long term plans for automation, but I've got my Plus Acct work flow getting pretty dialed in, at least for what I'm doing. Not counting 9/13 data I'm up to 1045 turns taken over a few 100 tasks in the last 6 days, every model has been used at least a few dozen times.

OpenAI may very well be messing around with usage limits, something could be bugged with the usage calculations or a much larger issue may be occurring with the models themselves...I dont know.  But I do know that these services are still at a point where if you just point them in a direction with a vague idea and give them broad access to unorganized areas and files on your PC, you're likely getting 1/5th or less out of it than you could.

- by [unknown](#) **&#x21C5; 1**
  <br/> can you share the exact write up you added to AGENTS.md?

- by [unknown](#) **&#x21C5; 1**
  <br/> You'll need to translate it:

## 2. Planificación


Todos los planes deben seguir por defecto este workflow: 
**GPT-6 Astra con thinking effort `low` para investigar, confirmar el diagnóstico y cerrar las decisiones; GPT-5.6 Luna con thinking effort `xhigh` para implementar el plan y ejecutar sus verificaciones**
, una vez solicitada la implementación. Respetar cualquier elección explícita posterior del usuario. Si la investigación presenta dudas complejas que no se consiguen resolver, explicar qué queda pendiente y recomendar aumentar el esfuerzo de Astra antes de dar el plan por preparado para Luna.


Consultar en cada planificación la documentación oficial actual de OpenAI mediante la skill 
**openai-docs**
 para verificar las capacidades y esfuerzos del workflow. Distinguir las capacidades documentadas del criterio aplicado a la tarea; no inventar comparaciones ni garantizar una implementación perfecta. Esta consulta no sustituye la elección de modelos establecida por el usuario. Indicar si la sesión activa usa otra configuración; escribir el plan no cambia por sí mismo el modelo ni el esfuerzo de la sesión. El workflow es secuencial y no autoriza subagentes ni delegación.


Crear en `PLAN_md` un plan de ejecución basado en el código actual del proyecto. Indicar el modelo y el esfuerzo recomendados, justificar brevemente la elección y enlazar las fuentes oficiales consultadas, distinguiendo las capacidades documentadas del criterio aplicado a la tarea. El plan debe contener las decisiones resueltas, los cambios por archivo, pasos pequeños y verificaciones concretas. Durante la planificación, no implementar todavía los cambios de la tarea.


Preparar cada plan con el máximo detalle útil para que Luna pueda ejecutarlo sin tener que rediseñar la solución ni repetir la investigación. Antes de cerrarlo, inspeccionar el código y confirmar las causas o necesidades relevantes; para problemas visuales o de ejecución, comprobar el comportamiento en navegador o en el entorno correspondiente cuando esté disponible. Separar hechos comprobados, hipótesis y bloqueos. No presentar como confirmado lo que solo se deduce del código o de una captura.


En todos los planes, concretar directamente el código de la lógica delicada o que requiera decisiones de razonamiento: indicar la ruta exacta, clase/función o ancla de inserción, qué bloque eliminar o sustituir y el código propuesto completo para ese bloque, incluidos imports, tipos y conexiones necesarias. Incluir ejemplos de pruebas para las invariantes difíciles. Estos bloques son propuestas dentro de PLAN_md; durante la planificación no aplicarlos al código de aplicación ni presentarlos como compilados o probados.


Para cambios pequeños, mostrar la sustitución o eliminación exacta. Para archivos nuevos cortos, incluir su contenido completo cuando cierre decisiones relevantes. Para cambios repetitivos o mecánicos, describir el patrón una sola vez y enumerar todos los archivos y símbolos a los que se aplica. No reproducir archivos largos enteros que apenas cambian, ni duplicar la misma implementación en varias secciones. Si el código propuesto precisa corregir una decisión anterior del plan, actualizar esa decisión para mantener una única solución coherente. Ante diferencias importantes con el árbol actual, revisar el bloque antes de aplicarlo: no reemplazar archivos completos a ciegas ni sobrescribir trabajo ajeno.


Cada plan debe incluir:


Para tareas de dificultad media o alta, es obligatorio entregar código propuesto completo de todos los bloques no mecánicos: estado y transiciones, efectos, temporizadores, asincronía, manejo de errores, integración entre componentes y pruebas de invariantes. Indicar por cada bloque archivo exacto, imports, tipos, ancla de inserción y qué función o fragmento se elimina o sustituye. No dejar instrucciones como «añadir un effect», «publicar transiciones» o «gestionar los errores» a decisión del implementador. Incluir HTML y SCSS completos de componentes nuevos cortos y ejemplos de pruebas ejecutables con sus mocks y preparación. Revisar antes de cerrar que los bloques encajan entre sí y con el código actual, sin decisiones esenciales pendientes ni contradicciones. El código de un plan es una propuesta: no afirmar que compila o pasa tests sin haberlo comprobado. En tareas simples, mantener sustituciones precisas y detalle proporcional; la obligación anterior sobre lógica delicada sigue aplicando.


- Alcance exacto, resultado esperado y comportamientos existentes que deben preservarse.
- Diagnóstico y evidencias, con rutas, símbolos y componentes actuales que se deben reutilizar.
- Decisiones técnicas resueltas y cambios concretos por archivo y función: contratos, tipos, flujo de datos, estilos o fragmentos de código cuando eliminen ambigüedad.
- Casos límite y tratamiento de valores vacíos, errores y datos existentes que afecten a la tarea.
- Pasos pequeños en orden de dependencia, con un resultado verificable para cada paso.
- Pruebas concretas: archivos de pruebas, preparación del entorno y datos, comandos ejecutables y resultados esperados. Incluir verificación visual cuando corresponda y criterios de aceptación observables.
- Límites de actuación: si el código ha cambiado o aparece una contradicción que invalida una decisión importante, detener el paso afectado, describir la evidencia y revisar el plan antes de improvisar una solución distinta.


Evitar instrucciones abiertas como «investigar», «ajustar según sea necesario» o «añadir pruebas» sin concretar qué comprobar, qué cambiar y cómo verificarlo. Si una decisión esencial sigue bloqueada, registrar la información que falta y no declarar el plan listo para implementación. El detalle debe resolver incertidumbre, sin repetir contenido ni ampliar el alcance. La finalización exige revisar el diff y los resultados reales de las verificaciones; no basta con la declaración de éxito del modelo implementador.


Presentar también en el chat el contenido sustancial del plan: alcance, decisiones, cambios por archivo o área, pasos de ejecución, verificaciones, modelo y esfuerzo recomendados con sus razones. El archivo de `PLAN_md` es el registro persistente, no un sustituto de explicar el plan al usuario en la conversación.


Explicar por separado y de forma concreta por qué se recomienda ese modelo y por qué se recomienda ese nivel de `thinking effort` para la tarea. Relacionar ambas razones con el alcance real, la complejidad, los riesgos, la calidad necesaria y el equilibrio entre coste y latencia; no limitarse a enumerar el modelo y el esfuerzo ni usar una justificación genérica. Incluir esta explicación tanto en el plan como en el resumen presentado al usuario, diferenciando el criterio propio de las capacidades confirmadas por las fuentes oficiales.

- by [unknown](#) **&#x21C5; 1**
  <br/> I have a $20 Gemini subscription and their Antigravity CLI tool.  I have Codex orchestrate code lookup and research to Gemini and let Gemini hold the code context, and Codex just asks for what it needs.  Saves me a LOT of Codex tokens this way, and I have never drained my Gemini limit.

- by [unknown](#) **&#x21C5; 1**
  <br/> How do you plan in one chat (codex) and implemented in another? I for example use the "plan" function but then have to click "implemented plan" in the same chat. How do you "store" the plan, simply in a text file/GitHub? Does it not lose a lot of important context?

And why is it better to do it your way, mabye because the planning context is condensed in the final plan and therefore less useless info = more context space for the implementation?

- by [unknown](#) **&#x21C5; 1**
  <br/> I had chatgpt write this out for orchestration and i would probably start a trial on a project using Sol low with this in agents.md:

Cost-Aware Agent Orchestration

Treat model capability as a scarce resource. Prefer the lowest-cost model that can reliably perform the task, while escalating when stronger reasoning materially improves correctness, architecture, or verification.

Default control flow  1. **Triage first.** The coordinating agent should first determine whether the task is:

    - simple and directly executable;
    - a bounded subtask of a larger problem;
    - complex enough to require stronger architectural reasoning.
  2. **Do not use frontier reasoning for routine work.** Use lower-cost agents for:

    - search, extraction, classification, formatting;
    - file inspection and chronology building;
    - repetitive coding or mechanical edits;
    - independent bounded research;
    - test execution and straightforward validation.
  3. **Escalate architecture, not entire workloads.** When a task is complex, consequential, ambiguous, or highly coupled, obtain a high-quality architecture/decomposition from a stronger model such as Sol/Astra. The architecture should define: After the architecture is established, return execution control to a cheaper coordinating agent wherever practical.

    - task DAG / dependency structure;
    - critical-path work;
    - parallelizable work;
    - acceptance criteria;
    - high-risk decisions;
    - conditions requiring re-escalation.
  4. **Delegate execution downward.** Prefer:

    - Luna-low/local-equivalent for trivial or mechanical work;
    - Luna for bounded reasoning and parallel workers;
    - Terra for coordination, reduction, integration, and intermediate review;
    - Sol/Astra for architecture, difficult reasoning, consequential judgment, or final high-value audit.
  5. **Separate roles where useful.** Do not assume the architect, scheduler, worker, and auditor must be the same model. Prefer the pattern: `cheap supervisor → strong architect → cheap/medium workers → medium verifier → strong audit only if warranted`
  6. **Avoid redundant expensive passes.** Do not invoke Sol/Astra separately for architecture and delegation planning unless the second call is justified. A strong architecture pass should normally provide enough structure for a cheaper coordinator to schedule and delegate the work.

Delegation economicsBefore spawning a subagent, consider:

  - expected difficulty;
  - consequence of error;
  - uncertainty;
  - decomposability;
  - opportunity for parallelism;
  - context required;
  - ease of independent verification;
  - coordination overhead;
  - likely token/model cost.

Spawn only when the expected improvement in quality or elapsed time reasonably exceeds coordination and inference cost.

Escalation ruleA lower-tier coordinator may escalate when it cannot reliably classify, decompose, execute, or verify a task.

Escalation should purchase the **smallest necessary unit of stronger reasoning**. After receiving that result, return remaining execution to cheaper agents whenever possible.

VerificationUse inexpensive verification where failure is readily detectable.

Escalate review to Terra or Sol/Astra when:

  - the result affects a consequential decision;
  - competing interpretations remain;
  - source material conflicts;
  - worker outputs disagree;
  - correctness cannot be established mechanically;
  - the task involves difficult legal, architectural, security, or other high-risk reasoning.

For critical work, the final reviewer should examine the synthesized result and relevant primary evidence rather than inheriting unverified worker conclusions.

Fan-out controlsAvoid uncontrolled recursive delegation.

Unless clearly justified:

  - prefer shallow delegation trees;
  - avoid workers spawning additional workers;
  - parallelize only genuinely independent work;
  - terminate workers that cease producing incremental value;
  - do not duplicate the same investigation across agents without an explicit comparison purpose.

Context disciplineProtect the coordinating model's context.

Workers should return:

  - conclusions;
  - evidence/source locations;
  - uncertainties;
  - failed approaches when materially relevant;
  - concise artifacts needed by subsequent stages.

Do not return large exploratory transcripts, redundant reasoning, or irrelevant intermediate material.

Governing principleSpend strong-model tokens primarily on decisions that improve many downstream tokens.

A short frontier-model architecture or audit that enables extensive lower-cost execution is preferable to having the frontier model perform routine work directly.
