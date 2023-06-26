#include "lists.h"

/**
 * cycle_check - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int cycle_check(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fst = list;

	if (!list)
		return (0);

	while (slw && fst && fst->next)
	{
		slw = slw->next;
		fst = fst->next->next;
		if (slw == fst)
			return (1);
	}

	return (0);
}
