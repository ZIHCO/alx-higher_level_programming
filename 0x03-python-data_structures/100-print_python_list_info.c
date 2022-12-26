#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

/**
 * print_python_list_info - C function that prints
 * some basic info about Python lists
 * @p: pointer the python list
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	int length;
	int allocated;

	length = PyList_Size(p);
	allocated = sizeof(p);

	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", p->allocated);
}
