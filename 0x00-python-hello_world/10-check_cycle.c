#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp;
	listint_t *check;

	if (list == NULL || list->next == NULL)
		return (0);
	tmp = list;
	check = tmp->next;

	while (tmp != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (tmp == check)
			return (1);
		tmp = tmp->next;
		check = check->next->next;
	}
	return (0);
}

