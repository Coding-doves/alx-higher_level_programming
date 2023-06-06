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

	while(ptr != NULL && ptr2 != NULL && ptr2->next != NULL && ptr->next != NULL)
	{
		ptr2 = ptr2->next;
		ptr = ptr->next->next;
		
		if(ptr2->next == ptr->next->next)
			return (1);
	}
	return (0);
}
