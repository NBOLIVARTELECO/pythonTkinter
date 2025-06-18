# 🐍 Python Tkinter Complete Tutorial

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-red.svg)

## 📋 Descripción

Este repositorio contiene un tutorial completo de **Tkinter**, la biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI). El proyecto incluye ejemplos prácticos de todos los widgets más importantes de Tkinter, organizados de manera didáctica y fácil de entender.

## 🚀 Características

- ✅ **Interfaz organizada por pestañas** para mejor navegación
- ✅ **Más de 15 tipos de widgets diferentes**
- ✅ **Ejemplos interactivos** con funcionalidad real
- ✅ **Código bien comentado** en español e inglés
- ✅ **Diseño moderno** con colores y estilos atractivos
- ✅ **Funcionalidades avanzadas** como diálogos y manejo de archivos

## 📁 Estructura del Proyecto

```
pythonTkinter/
├── tkinter_basics.py          # Tutorial principal con todos los widgets
├── tempCodeRunnerFile.py      # Archivo temporal (puede eliminarse)
└── README.md                  # Este archivo
```

## 🔧 Requisitos

- **Python 3.6 o superior**
- **Tkinter** (incluido por defecto en Python)
- **Sistema operativo**: Windows, macOS, o Linux

## 🏃‍♂️ Cómo ejecutar

1. **Clonar el repositorio:**
```bash
git clone https://github.com/NBOLIVARTELECO/pythonTkinter.git
cd pythonTkinter
```

2. **Ejecutar el tutorial:**
```bash
python tkinter_basics.py
```

## 📚 Contenido del Tutorial

### 🏷️ **Pestaña 1: Basic Widgets**

#### 📝 Widgets de Entrada
- **Entry**: Campo de texto de una línea
- **Text**: Área de texto multilínea
- **Button**: Botón interactivo con funcionalidad

#### 🎯 Widgets de Selección
- **Checkbutton**: Casillas de verificación múltiple
- **Radiobutton**: Botones de opción única
- **Listbox**: Lista seleccionable con scrollbar

### 🏷️ **Pestaña 2: Advanced Widgets**

#### 🎛️ Controles Avanzados
- **Scale**: Control deslizante para valores numéricos
- **Spinbox**: Selector numérico con flechas
- **Progressbar**: Barra de progreso animada
- **Combobox**: Lista desplegable (TTK)

### 🏷️ **Pestaña 3: Dialogs & Files**

#### 💬 Diálogos y Archivos
- **FileDialog**: Abrir y guardar archivos
- **ColorChooser**: Selector de colores
- **MessageBox**: Ventanas de mensaje
- **SimpleDialog**: Diálogos de entrada simple

## 🛠️ Widgets Incluidos

| Widget | Descripción | Uso Común |
|--------|-------------|-----------|
| `Label` | Mostrar texto o imágenes | Etiquetas descriptivas |
| `Entry` | Entrada de texto una línea | Campos de formulario |
| `Text` | Entrada de texto multilínea | Editores de texto |
| `Button` | Botón clickeable | Acciones del usuario |
| `Checkbutton` | Casilla de verificación | Opciones múltiples |
| `Radiobutton` | Botón de opción | Selección única |
| `Listbox` | Lista de elementos | Selección de listas |
| `Scale` | Control deslizante | Valores numéricos |
| `Spinbox` | Selector numérico | Números específicos |
| `Progressbar` | Barra de progreso | Indicador de progreso |
| `Combobox` | Lista desplegable | Selección con opciones |
| `Frame` | Contenedor de widgets | Organización visual |
| `LabelFrame` | Marco con etiqueta | Agrupación de controles |
| `Notebook` | Pestañas | Organización por secciones |

## 🎨 Características Especiales

### 🎯 Funcionalidades Implementadas

1. **Validación de Formularios**: Verificación de campos obligatorios
2. **Manejo de Archivos**: Abrir, guardar y procesar archivos
3. **Selector de Colores**: Cambio dinámico de colores
4. **Barra de Progreso**: Animación de tareas en progreso
5. **Resumen Completo**: Recopilación de todos los datos ingresados
6. **Reloj en Tiempo Real**: Actualización automática de la hora
7. **Scrollbars**: Navegación en contenido extenso

### 🎨 Diseño Visual

- **Colores modernos** con esquema coherente
- **Tipografía clara** con diferentes tamaños
- **Espaciado apropiado** para mejor legibilidad
- **Iconos emoji** para mejor experiencia visual
- **Organización por pestañas** para navegación fácil

## 🔍 Ejemplos de Código

### Crear una ventana básica:
```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Primera Ventana")
ventana.geometry("400x300")
ventana.mainloop()
```

### Añadir un botón con función:
```python
def mi_funcion():
    print("¡Botón presionado!")

boton = tk.Button(ventana, text="Click Me", command=mi_funcion)
boton.pack(pady=10)
```

### Crear un Entry con validación:
```python
entry = tk.Entry(ventana, font=("Arial", 12))
entry.pack(pady=5)

def validar_entrada():
    texto = entry.get()
    if texto:
        print(f"Entrada válida: {texto}")
    else:
        print("Por favor, ingresa algún texto")
```

## 🎓 Conceptos Aprendidos

Al completar este tutorial, habrás aprendido:

- ✅ **Creación de ventanas** y configuración básica
- ✅ **Uso de todos los widgets principales** de Tkinter
- ✅ **Manejo de eventos** y funciones callback
- ✅ **Organización de interfaces** con Frame y Notebook
- ✅ **Validación de formularios** y manejo de datos
- ✅ **Diálogos de archivos** y selección de colores
- ✅ **Gestión del layout** con pack(), grid(), y place()
- ✅ **Personalización visual** con colores y fuentes
- ✅ **Programación orientada a eventos** en GUI

## 🚀 Próximos Pasos

Para continuar aprendiendo, podrías explorar:

1. **Tkinter avanzado**: Canvas, menús, toolbar
2. **Otras bibliotecas GUI**: PyQt, Kivy, Dear PyGui
3. **Bases de datos**: Conectar tu GUI con SQLite
4. **Empaquetado**: Crear ejecutables con PyInstaller
5. **Diseño responsivo**: Interfaces que se adapten al tamaño

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres añadir más ejemplos o mejorar el código:

1. Fork el repositorio
2. Crea una rama para tu característica
3. Commit con cambios descriptivos
4. Push a la rama
5. Abre un Pull Request

## 📞 Soporte

Si tienes preguntas o encuentras algún problema:

- 📧 Abre un **Issue** en GitHub
- 💬 Revisa la **documentación oficial** de Tkinter
- 🔍 Busca en **Stack Overflow** para problemas específicos

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Puedes usarlo libremente para aprender y enseñar.

## 👨‍💻 Autor

**Néstor Bolívar** - [@NBOLIVARTELECO](https://github.com/NBOLIVARTELECO)

---

### 🌟 ¡Dale una estrella si te fue útil!

```python
print("¡Gracias por usar este tutorial de Tkinter!")
print("Happy Coding! 🐍✨")
```

---

*Última actualización: Junio 2025*
