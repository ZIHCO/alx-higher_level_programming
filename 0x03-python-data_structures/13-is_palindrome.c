#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: the listint_t
 * Return: 0 if not a palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *list;
	listint_t *list_reversed;

	if (*head)
	{
		list = *head;
		list_reversed = list_reversal(head);
		while (list)
		{
			if ((list->n) != (list_reversed->n))
				return (0);
			list_reversed = list_reversed->next;
			list = list->next;
		}
		return (1);
	}
	return (1);
}

/**
 * list_reversal - reverses a singly linked list
 * @head: the listint_t
 * Return: the pointer to the reversed list
 */
listint_t *list_reversal(listint_t **head)
{
	listint_t *prev_node = NULL; /* holds the new reversal head*/
	listint_t  *tmp; /* holds the head of the old list */
	listint_t *node; /* holds what node we are at */

	if (*head)
	{
		node = *head;
		while (node)
		{
			tmp = node->next;
			node->next = prev_node;
			prev_node = node;
			node = tmp;
		}
		*head = prev_node;
		return (*head);
	}
	return (NULL);
}
