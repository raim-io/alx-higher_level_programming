#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int compare_lists(listint_t *head1, listint_t *head2);
listint_t *reverse_list(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head;
	listint_t *second_half, *prev_of_slow = *head;
	listint_t *midnode = NULL; // To handle odd size list
	int res = 1;			   // Assume list is palindrome

	if (*head != NULL && (*head)->next != NULL)
	{
		// Find the middle of the list
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_of_slow = slow;
			slow = slow->next;
		}

		/* fast would be NULL when there are even elements in list.
		 * And not NULL for odd elements. We need to skip the middle node
		 * for odd case and store it somewhere in case we need to restore
		 * the original list */
		if (fast != NULL)
		{
			midnode = slow;
			slow = slow->next;
		}

		// Now reverse the second half and compare it with the first half
		second_half = slow;
		prev_of_slow->next = NULL;				 // NULL terminate first half
		reverse_list(&second_half);				 // Reverse the second half
		res = compare_lists(*head, second_half); // compare

		// Construct the original list back
		reverse_list(&second_half); // Reverse the second half again

		// If there was a mid node (odd size case) which
		// was not part of either first half or second half.
		if (midnode != NULL)
		{
			prev_of_slow->next = midnode;
			midnode->next = second_half;
		}
		else
		{
			prev_of_slow->next = second_half;
		}
	}

	return res;
}

/* Function to reverse the linked list */
listint_t *reverse_list(listint_t **head_ref)
{
	listint_t *prev = NULL;
	listint_t *current = *head_ref;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head_ref = prev;
	return *head_ref;
}

/* Function to check if two input lists have same data */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return 0;
		}
	}

	// Both are empty return 1
	if (temp1 == NULL && temp2 == NULL)
	{
		return 1;
	}

	// Will reach here when one is NULL and other is not
	return 0;
}
