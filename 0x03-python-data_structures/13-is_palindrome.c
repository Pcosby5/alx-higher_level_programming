#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = *head;
    listint_t *second_half = NULL, *mid_node = NULL, *current, *temp;
    int is_palindrome = 1;

    /* Check if the list is empty or contains only one element */
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    /* Find the middle of the list using slow and fast pointers */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    /* If the list has an odd number of elements, set mid_node */
    if (fast != NULL)
    {
        mid_node = slow;
        slow = slow->next;
    }

    /* Divide the list into two parts and reverse the second part */
    second_half = slow;
    prev->next = NULL;
    prev = NULL;
    current = second_half;
    while (current)
    {
        temp = current->next;
        current->next = prev;
        prev = current;
        current = temp;
    }
    second_half = prev;

    /* Compare the first and reversed second parts of the list */
    is_palindrome = compare_linked_lists(*head, second_half);

    /* Restore the original list by connecting the parts */
    prev = NULL;
    current = second_half;
    while (current)
    {
        temp = current->next;
        current->next = prev;
        prev = current;
        current = temp;
    }
    second_half = prev;

    /* If mid_node is not NULL, reconnect it in the middle */
    if (mid_node)
    {
        prev->next = mid_node;
        mid_node->next = second_half;
    }
    else
    {
        prev->next = second_half;
    }

    return is_palindrome;
}

/**
 * compare_linked_lists - function to compare two linked lists
 * @list1: first list
 * @list2: second list
 * Return: 1 if they match, 0 if they do not match
 */
int compare_linked_lists(listint_t *list1, listint_t *list2)
{
    listint_t *temp1 = list1, *temp2 = list2;

    while (temp1 && temp2)
    {
        if (temp1->n != temp2->n)
            return (0);
        temp1 = temp1->next;
        temp2 = temp2->next;
    }

    /* Both lists should be NULL if they match completely */
    return (temp1 == NULL && temp2 == NULL);
}
