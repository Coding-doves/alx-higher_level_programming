#include "lists.h"
#include <stddef.h>
/**
 * insert_node - add a data to a sorted singly linked list
 * @head: start of list
 * @number: data to add
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr;
	listint_t *val = malloc(sizeof(listint_t));

	if (head == NULL || val == NULL)
		return (NULL);

	val->n = number;
	val->next = NULL;

	/* if the list is empty, update it*/
	if (*head == NULL)
	{
		*head = val;
		return (val);
	}

	ptr = *head;
	/* update head->next to a new data/node*/
	if (val->n < ptr->n)
	{
		val->next = ptr;
		*head = val;
	}

	while (ptr->next != NULL)
	{
		if (ptr->n <= val->n && ptr->next->n >= val->n)
		{
			val->next = ptr->next;
			ptr->next = val;
			return (val);
		}

		ptr = ptr->next;

	}
	ptr->next = val;/*insert node at the end if it is the largest*/

	return (val);
}
