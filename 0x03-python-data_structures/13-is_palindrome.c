#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - checks if a string can be read forward and backwards
 * @head: start of our linked list
 * Return: 0 (false) if it is not a palindrome, 1 (true) if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *ptr2;
	listint_t *front, *back = NULL;

	if (head == NULL || (*head)->next == NULL)
		return (1);

	ptr = *head;
	/*revesering linked list*/
	while (ptr != NULL)
	{
		front = ptr->next;
		ptr->next = back;
		back = ptr;
		ptr = front;
	}
	ptr = back;

	ptr2 = *head;
	/* compare reversed list with original list*/
	while (ptr->next && ptr2->next)
	{
		if (ptr->next != ptr2->next)
		{
			return (0);
			break;
		}
		ptr = ptr->next;
		ptr2 = ptr2->next;
	}
	return (1);
}
