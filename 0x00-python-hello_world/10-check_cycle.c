#include "lists.h"

/**
 * check_cycle - check if a list has cycular linked list
 * @list: linked list input
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr, *ptr2;

	ptr = ptr2 = list;

	while (ptr2 != NULL && ptr2->next != NULL)
	{
		ptr = ptr->next;
		ptr2 = ptr2->next->next;
		if (ptr == ptr2)
			return (1);
	}
	return (0);
}
