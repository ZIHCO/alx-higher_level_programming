#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the head to the list
 * Return: 1 if true or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slownode = list;
	listint_t *fastnode = list;

	if (list)
	{
		while (slownode && fastnode && fastnode->next)
		{
			slownode = slownode->next;
			fastnode = fastnode->next->next;
			if (fastnode == slownode)
				return (1);
		}
	}
	return (0);
}
