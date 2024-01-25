#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    // Check if p is a list
    if (PyList_Check(p))
	{
        Py_ssize_t size = PyList_Size(p);
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

        for (Py_ssize_t i = 0; i < size; i++)
		{
            PyObject *item = PyList_GET_ITEM(p, i);
            printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
        }
    } else
	{
        printf("[ERROR] Invalid List Object\n");
    }
}

void print_python_bytes(PyObject *p)
{
    // Check if p is a bytes object
    if (PyBytes_Check(p))
	{
        Py_ssize_t size = PyBytes_Size(p);
        printf("[.] bytes object info\n");
        printf("  size: %zd\n", size);

        char *trying_str = PyBytes_AsString(p);
        printf("  trying string: %s\n", trying_str);

        printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
        for (Py_ssize_t i = 0; i < size && i < 10; i++)
		{
            printf(" %02x", (unsigned char)trying_str[i]);
        }
        printf("\n");
    } else
	{
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}
