#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

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
		list_reversed = list_reversal(&list);
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
	listint_t  *tmp;
	listint_t *new;

	if (*head)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = (*head)->n;
		new->next = NULL;
		tmp = (*head)->next;
		while (tmp)
		{
			add_nodeint(&new, (tmp->n));
			tmp = tmp->next;
		}
		return (new);
	}
	return (NULL);
}

/**
 * add_nodeint - adds new node at the beginning of list
 * @head: ...
 * @n: ....
 * Return: address of new node
 */
listint_t *add_nodeint(listint_t **head, int n)
{
	listint_t *new;

	if (head)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);

		new->n = n;
		new->next = *head;
		*head = new;
		return (new);
	}
	return (NULL);
}
