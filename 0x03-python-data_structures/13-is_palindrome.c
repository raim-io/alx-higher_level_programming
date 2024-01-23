#include "lists.h"

/**
 * reverse_list - reverses the second half of the list
 *
 * @half_head: head of the second half
 * Return: no return
 */
void reverse_list(listint_t **half_head)
{
	listint_t *prev;
	listint_t *curr;
	listint_t *nxt;

	prev = NULL;
	curr = *half_head;

	while (curr != NULL)
	{
		nxt = curr->next;
		curr->next = prev;
		prev = curr;
		curr = nxt;
	}

	*half_head = prev;
}

/**
 * compare_lists - compares each int of the list
 *
 * @head1: pointer to d head of the first half
 * @head2: pointer to d head of the second half
 * Return: 1 if are equals, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1;
	listint_t *temp2;

	temp1 = head1;
	temp2 = head2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (temp1 == NULL && temp2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if a singly linked
 * list is a palindrome.
 * @head: pointer to the head of the list
 * Return: 1 if it is a palndrome,
 * 0 if it is not a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scn_half, *middle;
	int is_pal;

	slow = fast = prev_slow = *head;
	middle = NULL;
	is_pal = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		scn_half = slow;
		prev_slow->next = NULL;
		reverse_list(&scn_half);
		is_pal = compare_lists(*head, scn_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = scn_half;
		}
		else
		{
			prev_slow->next = scn_half;
		}
	}

	return (is_pal);
}
