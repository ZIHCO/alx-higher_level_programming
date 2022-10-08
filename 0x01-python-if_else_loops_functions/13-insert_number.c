#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the head
 * @number: data
 * Return: address of a new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp;
	listint_t *node;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head)
	{
		tmp = (*head)->next;
		node = *head;
		if ((node->n) > number)
		{
			new->next = node;
			*head = new;
			return (new);
		}
		while (tmp)
		{
			if ((tmp->n) < number)
			{
				node = node->next;
				tmp = tmp->next;
			}
			else
			{
				new->next = tmp;
				node->next = new;
				return (new);
			}
		}
		node->next = new;
		new->next = NULL;
		return (new);
	}
	new->next = NULL;
	*head = new;
	return (new);
}
