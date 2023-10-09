# Proyecto Ética y Seguridad de los Datos: Health Insurance Cross Sell Prediction

## Contexto e Introducción al Proyecto

El proyecto se centra en el análisis del dataset [Health Insurance Cross Sell Prediction](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction) que contiene 381,000 filas, con el objetivo de optimizar la estrategia de canales de ventas, segmentar eficientemente a los clientes, mejorar la rentabilidad de pólizas/promociones y predecir la retención de clientes.

## Sobre la base de datos y las transformaciones necesarias

El dataset original contiene las siguientes variables:

| Variable              | Descripción                                                   |
|----------------------|---------------------------------------------------------------|
| Gender               | Género del cliente                                            |
| Age                  | Edad del cliente                                              |
| Previously_Insured   | 1 : Cliente tiene seguro de vehículo, 0 : Cliente no tiene seguro de vehículo |
| Vehicle_Age          | Tiempo del vehículo                                           |
| Vehicle_Damage       | 1 : Cliente dañó su vehículo en el pasado. 0 : Cliente no dañó su vehículo en el pasado |
| Annual_Premium       | Monto que necesita pagar el cliente como premium en el año   |
| Policy_Sales_Channel | Código anónimo del canal de comunicación con el cliente (Correo, persona, teléfono, etc) |
| Vintage              | Número de días que el cliente ha estado asociado con la compañía |
| Response             | 1 : Cliente interesado, 0 : Cliente no interesado              |


Sobre la data real, se agregará data mock que puede ser considerada sensible sobre cada cliente incluyendo:

| Variable       | Descripción                                      |
|---------------|--------------------------------------------------|
| First name    | Nombre de la persona                             |
| Last name     | Apellido de la persona                           |
| Phone_Number  | Celular de la persona                            |
| CCNumber      | Número de tarjeta de crédito                     |
| Address       | Dirección de la persona                          |
| Country       | Abreviatura del país donde vive                  |
| Email         | Correo electrónico de la persona                 |

Más adelante, se planea agregar un VIN (Vehicle Identification Number) para cada vehículo y el SSN (Social Security Number) para cada persona.

La estructura de la base de datos se detalla en las siguientes tablas:

```sql
CREATE TABLE `users` (
  `id` int PRIMARY KEY,
  `first_name` varchar(255),
  `last_name` varchar(255),
   `password` varchar(256),
  `phone` varchar(255),
  `email` varchar(255),
  `gender` varchar(255),
  `age` int,
  `address` varchar(255),
  `country` varchar(255),
  `ccnumber` varchar(255)
);

CREATE TABLE `vehicle_info` (
  `id` int PRIMARY KEY,
  `user_id` int,
  `vehicle_age` varchar(255),
  `vehicle_damage` varchar(255)
);

CREATE TABLE `insurance_info` (
  `id` int PRIMARY KEY,
  `user_id` int,
  `driving_license` int,
  `previously_insured` int,
  `annual_premium` float,
  `policy_sales_channel` float,
  `vintage` int,
  `response` int
);

ALTER TABLE `users` ADD FOREIGN KEY (`id`) REFERENCES `insurance_info` (`user_id`);

ALTER TABLE `users` ADD FOREIGN KEY (`id`) REFERENCES `vehicle_info` (`user_id`);
```

### Diagrama E-R

![Diagrama E-R](anexos/try2.png)


## Requerimientos de Negocio

Los KPIs definidos son:

- Optimización en la Estrategia de Canales de Ventas.
- Segmentación eficiente de clientes.
- Mejorar la rentabilidad de “Pólizas/Promociones”.
- Predicción de Retención de Clientes.

## Requerimientos de Seguridad

### En Reposo:

- Cifrado de datos en AWS.
- AWS Key Management Service (Keyvault).
- Configuración adecuada de los IAM.
- Almacenamiento apropiado de logs (alternativa a CloudWatch si no es suficiente).
- Hashing de usuarios.

### En Transporte:

- HTTPS (si es posible en el tiempo dado).
- Verificación de emisor y receptor.
- Grupos de seguridad en AWS como firewall.

### Gestión de Accesos:

- RBAC, ABAC.
- MFA.
- OTP.

### Logs y Auditoría:

- Herramienta para revisión de logs.
- Sistema de alertas.


## Estrategias de uso seguro de los datos

Se detallan las políticas, procedimientos y estándares, y la concienciación y formación del equipo respecto a la seguridad de los datos.

### Políticas
Desarrolla políticas claras y sólidas que establezcan las reglas y normativas para el acceso, uso y manejo de los datos.

- Requiere autenticación de dos factores (2FA) para el acceso a sistemas y aplicaciones que almacenan datos sensibles.
- Establece reglas de acceso basadas en roles para garantizar que solo las personas autorizadas tengan acceso a datos específicos.
- Requiere contraseñas fuertes y periódicamente cambiantes.
- Prohíbe el uso compartido de contraseñas y la escritura de contraseñas en papel o medios no seguros.
- Exige el cifrado de datos sensibles tanto en reposo como en tránsito.
- Define algoritmos y estándares de cifrado a utilizar.
- Establece la frecuencia de copias de seguridad y procedimientos de recuperación de datos en caso de fallos o incidentes.
- Asegura que las copias de seguridad se almacenan en ubicaciones seguras.
- Regula el acceso de proveedores externos y contratistas a los sistemas y datos de la organización.
- Exige acuerdos de confidencialidad y seguridad con terceros que manejen datos sensibles.

### Procedimientos y estándares

Crea procedimientos detallados para la recopilación, almacenamiento, transmisión y eliminación segura de datos e implementa estándares de seguridad de datos reconocidos, como ISO 27001, para garantizar buenas prácticas.

- Creación y gestión de credenciales de usuario, junto con su autenticación en sistemas y aplicaciones.
- Creación, cambio y gestión de contraseñas de usuario teniendo en cuenta la prohibición de compartir contraseñas.
- Configuración y mantenimiento de la infraestructura de cifrado.
- Realización de copias de seguridad regulares y restauración de datos en caso de pérdida o corrupción.
- Reglamento General de Protección de Datos (GDPR) de la Unión Europea: El GDPR es una regulación de la UE que establece estándares para la protección de datos personales.
- AES (Advanced Encryption Standard): AES es uno de los estándares de encriptación más ampliamente utilizados en todo el mundo.
- RSA (Rivest-Shamir-Adleman): RSA es un estándar de encriptación asimétrica que se utiliza para la encriptación de datos y la autenticación.
- El conjunto de estándares PKCS (Public Key Cryptography Standards)

### Concientización y formación del equipo

Proporciona capacitación y concienciación sobre seguridad de datos a todos los miembros del equipo, desde empleados hasta directivos y se fomenta una cultura de seguridad de datos en la que todos comprendan la importancia de proteger la información.

- Se cubren temas como la gestión de contraseñas, la identificación de correos electrónicos de phishing y las mejores prácticas de seguridad en general.
- Realiza simulaciones de ataques de phishing para ayudar a los empleados a reconocer correos electrónicos maliciosos y a tomar decisiones seguras, con ello, se proporciona retroalimentación y refuerza las prácticas correctas.
- Utiliza juegos y ejercicios interactivos para enseñar conceptos de seguridad de datos de manera divertida y memorable.
- Comparte historias de casos y ejemplos reales de incidentes de seguridad de datos, tanto internos como externos, para ilustrar las amenazas y sus impactos.
- Proporciona a los empleados materiales educativos, como folletos, infografías y videos, que resuman las mejores prácticas de seguridad.
- Realiza pruebas periódicas de conocimientos para medir la comprensión de los empleados sobre seguridad de datos. Luego, se proporciona retroalimentación y refuerza las áreas que necesitan mejora.
- Asegurarse de que los empleados estén al tanto de las políticas de uso aceptable de la tecnología y de las consecuencias de su incumplimiento.
- Proporciona formación especializada a los equipos de TI y seguridad de datos para mantenerlos al tanto de las últimas amenazas y técnicas de mitigación.

## Plan de respuesta ante incidentes de seguridad

En caso de una fuga o pérdida de datos, se plantea el siguiente plan básico de acción:

1. **Confirmar la fuga o pérdida de los datos y evaluar la magnitud del evento:**
    - De esta manera, determinamos cuáles y cuántos datos han sido afectados, si se trata de datos privados de los usuarios o datos internos de la aseguradora, y cuándo ocurrió la fuga para entender la gravedad del incidente.
2. **Aislamiento y Mitigación del daño sobre las áreas afectadas:**
    - Al aislar las áreas afectadas evitamos que el daño pueda convertirse en colateral y afectar otras áreas o procesos del servicio web. A su vez, se toma medidas para mitigar cualquier daño adicional o propagación de la fuga, mediante desconexiones de sistemas, cambios de contraseñas y cambios en las restricciones de acceso.
3. **Notificación a las partes afectadas:**
    - Comunicar a las partes interesadas de la aseguradora y, de ser necesario, también a los clientes afectados de manera transparente y oportuna, informando que el servicio web podría encontrarse caído por un tiempo hasta que se contenga y arregle el daño.
4. **Realizar una investigación interna sobre los Logs del sistema:**
    - De esta manera, mediante análisis forense, se puede identificar las causas de la fuga, quiénes estuvieron involucrados, la debilidad en la zona vulnerada y, más adelante, se puede plantear cómo se pudo haber prevenido.
5. **Reparación y Mejoras:**
    - Realizar las correcciones necesarias para evitar futuras fugas de datos, ya sea que haya ocurrido de manera intencional o no intencional, y se pueda mejorar la seguridad del sistema.
6. **Monitoreo Continuo:**
    - Si bien se espera que esa área esté arreglada y protegida de cualquier daño, es importante que después de un evento similar se mantenga un monitoreo más intencional sobre el área afectada, así se pueda detectar de manera más proactiva cualquier actividad que se considere fuera de lo común.

## Recomendaciones de Protección de Datos Futura

- VPN, WAF, Tokenización de datos sensibles.
- (Pseudo) Anonimización de datos, IDS/IPS, Pruebas de penetración periódicas.
- Gestión mejorada de claves y certificados.

## Lecciones Aprendidas y Retrospectiva

a



&copy; 2023 Proyecto DS3031
