# Python Script to Brute Force Login Panel (PortSwigger Lab)

Este script de Python está diseñado para completar el laboratorio de PortSwigger: **"Username enumeration via different responses"**.

En este ejercicio, se proporciona un listado de nombres de usuario y contraseñas. El objetivo es utilizarlos en un panel de login para acceder como otro usuario y completar el laboratorio.

### Enlace al laboratorio:
[PortSwigger Lab](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses)

---

## 📋 Requerimientos

El script requiere algunas librerías adicionales para su funcionamiento, como **pwntools**, que no está incluida en la biblioteca estándar de Python. Para facilitar la instalación, se incluye un archivo `requirements.txt`.

### Instalación de dependencias

Ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip3 install -r requirements.txt
```

---

## 🚀 Uso

El script es muy sencillo de usar. Solo necesitas proporcionar la URL del panel de login de tu laboratorio de PortSwigger.

### Comando de ejemplo:

```bash
python3 brute_force.py -u https://0a7f00a803ef9b1dd5820d0d008c0040.web-security-academy.net/login
```

---

## ⚙️ Funcionamiento

El script realiza dos pasos principales:

1. **Identificación de usuarios válidos:** Utiliza técnicas de enumeración para descubrir qué nombres de usuario son válidos en el sistema.
2. **Descubrimiento de contraseñas:** Prueba combinaciones de contraseñas con los usuarios válidos para identificar credenciales correctas.

### Ejemplo de salida:

```bash
[>] User: ar
[q] Password: jennifer
[◐] Valid Users: ar

[+] VALID CREDENTIALS:
    username: ar
    password: jennifer
```

---

## ⚠️ Advertencia

Este script debe ser utilizado **únicamente** en entornos de pruebas autorizados, como los laboratorios de PortSwigger. El uso no autorizado de esta herramienta contra sistemas reales es **ilegal** y puede tener consecuencias graves.
