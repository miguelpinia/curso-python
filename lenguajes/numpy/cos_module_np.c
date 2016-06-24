/*  Ejemplo de uso de la función cos de math.h usando la Numpy-C-API */

#include <Python.h>
#include <numpy/arrayobject.h>
#include <math.h>

/*  Funcíon coseno envuelta */
static PyObject* cos_func_np(PyObject* self, PyObject* args)
{

    PyArrayObject *in_array;
    PyObject      *out_array;
    NpyIter *in_iter;
    NpyIter *out_iter;
    NpyIter_IterNextFunc *in_iternext;
    NpyIter_IterNextFunc *out_iternext;

    if (!PyArg_ParseTuple(args, "O!", &PyArray_Type, &in_array))
        return NULL;

    out_array = PyArray_NewLikeArray(in_array, NPY_ANYORDER, NULL, 0);
    if (out_array == NULL)
        return NULL;

    in_iter = NpyIter_New(in_array, NPY_ITER_READONLY, NPY_KEEPORDER,
                             NPY_NO_CASTING, NULL);
    if (in_iter == NULL)
        goto fail;

    out_iter = NpyIter_New((PyArrayObject *)out_array, NPY_ITER_READWRITE,
                          NPY_KEEPORDER, NPY_NO_CASTING, NULL);
    if (out_iter == NULL) {
        NpyIter_Deallocate(in_iter);
        goto fail;
    }

    in_iternext = NpyIter_GetIterNext(in_iter, NULL);
    out_iternext = NpyIter_GetIterNext(out_iter, NULL);
    if (in_iternext == NULL || out_iternext == NULL) {
        NpyIter_Deallocate(in_iter);
        NpyIter_Deallocate(out_iter);
        goto fail;
    }
    double ** in_dataptr = (double **) NpyIter_GetDataPtrArray(in_iter);
    double ** out_dataptr = (double **) NpyIter_GetDataPtrArray(out_iter);

    do {
        **out_dataptr = cos(**in_dataptr);
    } while(in_iternext(in_iter) && out_iternext(out_iter));

    NpyIter_Deallocate(in_iter);
    NpyIter_Deallocate(out_iter);
    Py_INCREF(out_array);
    return out_array;

    fail:
        Py_XDECREF(out_array);
        return NULL;
}

static PyMethodDef CosMethods[] =
{
     {"cos_func_np", cos_func_np, METH_VARARGS,
         "evaluate the cosine on a numpy array"},
     {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initcos_module_np(void)
{
     (void) Py_InitModule("cos_module_np", CosMethods);
     /* IMPORTANT: this must be called */
     import_array();
}
