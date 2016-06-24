/* Ejemplo de la función coseno de math.h envuelta con la Python C-API. */
#include <Python.h>
#include <math.h>

/*  Función coseno envuelta. */
static PyObject* cos_func(PyObject* self, PyObject* args)
{
    double value;
    double answer;

    /*  Transforma la entrada, desde un float de python a un double de C */
    if (!PyArg_ParseTuple(args, "d", &value))
        return NULL;
    /* Si la función anterior regresa -1, una excepción apropiada de
     * Python va ser lanzada y la función simplemente regresa NULL
     */

    /* LLamamos cos desde la biblioteca libm */
    answer = cos(value);

    /*  Construye la salida de coseno, desde un double de C a un float de Python */
    return Py_BuildValue("f", answer);
}

/*  Define la función en el módulo */
static PyMethodDef CosMethods[] =
{
     {"cos_func", cos_func, METH_VARARGS, "Evalua el coseno"},
     {NULL, NULL, 0, NULL}
};

/* Incialización del módulo */
PyMODINIT_FUNC

initcos_module(void)
{
     (void) Py_InitModule("cos_module", CosMethods);
}
