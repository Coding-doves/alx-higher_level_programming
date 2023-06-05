#include "lists.h"

/**
 * check_cycle - check if a list has cycle
 * @list: linked list input
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr = list;

	while(ptr->next != NULL)
	{
		ptr = ptr->next;
		if(ptr->next == list)
			return (0);
	}
	return (-1);
}
