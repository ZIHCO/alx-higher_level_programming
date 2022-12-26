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
	int length, allocate, i;
	PyListObject *p_list;

	length = PyList_Size(p);
	p_list = (PyListObject *) p;
	allocate = p_list->allocated;

	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", allocate);

	for (i = 0; i < length; i++)
	{
		printf("Element %d: %s\n", i,
		       (PyList_GET_ITEM(p, i))->ob_type->tp_name);
	}
}
