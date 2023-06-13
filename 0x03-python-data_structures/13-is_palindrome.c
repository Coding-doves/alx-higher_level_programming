#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - checks if a string can be read forward and backwards
 * @head: start of our linked list
 * Return: 0 (false) if it is not a palindrome, 1 (true) if it is a palindrome
 */


/* reversing the whole list before checking (big O(n))*/
/*
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *ptr2;
	listint_t *front, *back = NULL;
	int i, len;

	ptr = *head;
	while (ptr != NULL)
	{
		i++;
		ptr = ptr->next;
	}

	if (head == NULL || (*head)->next == NULL)
		return (1);
*/
	/*revesering linked list*/
/*	while (ptr != NULL)
	{
		front = ptr->next;
		ptr->next = back;
		back = ptr;
		ptr = front;
	}
	ptr = back;

	ptr2 = *head;*/
	/* compare reversed list with original list*/
/*	len = i / 2;
 *	while (len > 0)
	{
		if (ptr->n != ptr2->n)
		{
			return (0);
			break;
		}
		ptr = ptr->next;
		ptr2 = ptr2->next;
	}
	return (1);
}*/




/* checking palindrome from the middle*/
/*
int is_palindrome(listint_t **head)
{
	listint_t *move1, *move2, *middle, *mid_nxt, *mid_prev, *ptr;

	if (head || *head)
		return (1);
	
	move1 = *head;
	move2 = *head;
*/	/* find the middle of our list*/
/*	while (1)
	{
		move2 = move2->next->next;
*/		/*odd list*/
/*		if (move2->next == NULL)
		{
			middle = move1->next->next;
			break;
		}
*/		/*even list*/
/*		if (move2 == NULL)
		{
			middle = move1->next;
			break;
		}
		move1 = move1->next;
	}
	move1 = NULL;
*/
	/*reverse the second half of the list*/
/*	mid_prev = NULL;
	while (middle != NULL)
	{
		mid_nxt = middle->next;
		middle->next = mid_prev;
		mid_prev = middle;
		middle = mid_nxt;
	}
	middle = mid_prev;
*/
	/*compare the two halves list*/
/*	ptr = *head;
	while (ptr != NULL && middle != NULL)
	{
		if (ptr->n != middle->n )
			return (0);
		ptr = ptr->next;
		middle = middle->next;
	}
	return (1);
}
*/

/* storing array before checking*/

int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head;
	int list[1024], i = 0, j, len;

	while (ptr != NULL && i < 1024)
	{	
		list[i++] = ptr->n;
		ptr = ptr->next;
	}

	len = i / 2;
	for (j = 0; j <= len; j++)
	{
		if (list[j] != list[i - j - 1])
			return (0);
	}

	return (1);
}
