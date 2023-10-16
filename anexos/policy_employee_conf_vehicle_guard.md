**Política de Confidencialidad para Empleados Vehicle Guard**


**Resumen y Propósito de la Política**

Diseñamos nuestra política de confidencialidad de la empresa para explicar cómo esperamos que nuestros empleados traten la información confidencial. Los empleados inevitablemente recibirán y manejarán información personal y privada sobre clientes, socios y nuestra empresa. Queremos asegurarnos de que esta información esté bien protegida.

Debemos proteger esta información por dos razones. Puede:
- Ser legalmente vinculante (por ejemplo, datos sensibles de los clientes).
- Constituir la columna vertebral de nuestro negocio, dándonos una ventaja competitiva (por ejemplo, procesos empresariales).

**Ámbito**

Esta política afecta a todos los empleados, incluidos los miembros de la junta, inversores, contratistas y voluntarios, que puedan tener acceso a información confidencial.

**Elementos de la Política**

La información confidencial y propietaria es secreta, valiosa, costosa y/o fácilmente replicable. Ejemplos comunes de información confidencial son:
- Información financiera no publicada
- Datos de Clientes/Socios/Proveedores
- Patentes, fórmulas o nuevas tecnologías
- Listas de clientes (existentes y potenciales)
- Datos confiados a nuestra empresa por partes externas
- Estrategias de precios/marketing y otras no reveladas
- Documentos y procesos marcados explícitamente como confidenciales
- Metas, pronósticos e iniciativas no publicadas marcadas como confidenciales

Los empleados pueden tener varios niveles de acceso autorizado a información confidencial.

**Lo que los empleados deben hacer:**
- Bloquear o asegurar la información confidencial en todo momento
- Destruir documentos confidenciales cuando ya no sean necesarios
- Asegurarse de que solo visualizan información confidencial en dispositivos seguros
- Solo divulgar información a otros empleados cuando sea necesario y autorizado
- Mantener documentos confidenciales dentro de las instalaciones de nuestra empresa a menos que sea absolutamente necesario moverlos

**Lo que los empleados no deben hacer:**
- Usar información confidencial para cualquier beneficio personal o ganancia
- Divulgar información confidencial a cualquier persona fuera de nuestra empresa
- Replicar documentos y archivos confidenciales y almacenarlos en dispositivos inseguros

Cuando los empleados dejen de trabajar para nuestra empresa, están obligados a devolver cualquier archivo confidencial y eliminarlos de sus dispositivos personales.

**Medidas de Confidencialidad**

Tomaremos medidas para garantizar que la información confidencial esté bien protegida. Nosotros:
- Almacenaremos y bloquearemos documentos en papel
- Encriptaremos la información electrónica y protegeremos las bases de datos
- Pediremos a los empleados que firmen acuerdos de no competencia y/o de no divulgación (NDA)
- Pediremos autorización de la alta dirección para permitir a los empleados acceder a cierta información confidencial

**Excepciones**

Ocasionalmente, la información confidencial puede tener que ser divulgada por motivos legítimos. Ejemplos son:
- Si un organismo regulador lo solicita como parte de una investigación o auditoría
- Si nuestra empresa examina una empresa conjunta o asociación que requiere divulgar cierta información (dentro de los límites legales)

En tales casos, los empleados involucrados deben documentar su procedimiento de divulgación y recopilar todas las autorizaciones necesarias. Estamos obligados a evitar divulgar más información de la necesaria.

**Consecuencias Disciplinarias**

Los empleados que no respeten nuestra política de confidencialidad enfrentarán acciones disciplinarias y, posiblemente, legales.

Investigaremos cada violación de esta política. Despediremos a cualquier empleado que infrinja voluntaria o regularmente nuestras pautas de confidencialidad para obtener beneficios personales. También podríamos tener que castigar cualquier violación no intencionada de esta política, dependiendo de su frecuencia y gravedad. Despediremos a los empleados que desatiendan repetidamente esta política, incluso cuando lo hagan sin intención.

Esta política es vinculante incluso después de la separación del empleo.

---

**Descargo de responsabilidad:** Esta plantilla de política de confidencialidad tiene como objetivo proporcionar pautas generales y debe usarse como referencia. Puede que no tenga en cuenta todas las leyes locales, estatales o federales relevantes y no es un documento legal. Ni el autor ni [Nombre de la Compañía] asumirán ninguna responsabilidad legal que pueda surgir del uso de esta política.

---

**Estándares de Seguridad Implementados:**

### En Reposo:

- **Cifrado de Datos en AWS:** Todas las informaciones confidenciales almacenadas en los sistemas de la empresa estarán cifradas utilizando los servicios de cifrado proporcionados por AWS.
- **AWS Key Management Service (Keyvault):** Se utilizará AWS Key Management Service para gestionar las claves de cifrado de forma segura.
- **Configuración adecuada de los IAM (Identity and Access Management):** Se implementarán políticas de IAM para asegurar que sólo los empleados autorizados tengan acceso a información confidencial.
- **Almacenamiento apropiado de logs:** Se almacenarán logs de todas las actividades relacionadas con el acceso y manipulación de información confidencial, utilizando CloudWatch o una alternativa si no es suficiente.
- **Hashing de Usuarios:** Las contraseñas y otros datos sensibles de los empleados serán hasheados para garantizar su seguridad.

### En Transporte:

- **HTTPS:** Todas las transmisiones de datos confidenciales se realizarán a través de conexiones seguras HTTPS.
- **Verificación de emisor y receptor:** Se implementarán medidas para verificar la identidad del emisor y del receptor antes de permitir la transmisión de información confidencial.
- **Grupos de Seguridad en AWS:** Se utilizarán grupos de seguridad en AWS como firewall para proteger los datos en tránsito.

### Gestión de Accesos:

- **RBAC, ABAC:** Se implementarán controles de acceso basados en roles (RBAC) y controles de acceso basados en atributos (ABAC) para gestionar el acceso a información confidencial.
- **OTP (One-Time Password):** Se utilizarán contraseñas de un solo uso para autenticar a los empleados antes de permitir el acceso a información confidencial.

### Logs y Auditoría:

- **Herramienta para revisión de logs:** Se implementará una herramienta para revisar los logs y monitorizar el acceso y manipulación de información confidencial.
- **Sistema de Alertas:** Se implementará un sistema de alertas para notificar a los administradores de cualquier actividad sospechosa o no autorizada.

--