package interfaces;

/**
 * An interface for the ADT List.
 */
public interface ListInterface<T>
{
    /**
     * Adds the new entry to the end of the list.
     *
     * @param newEntry the entry to add
     * @return true if the entry was added successfully, false otherwise
     */
    boolean add(T newEntry);

    /**
     * Adds the specified entry at the specified position in the list.
     * Shifts the entry currently at that position (if any) and any subsequent
     * entries to the right (adds one to their indices).
     *
     * @param index the index at which to add the entry
     * @param newEntry the entry to add
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    void add(int index, T newEntry);

    /**
     * Returns the entry at the specified position in the list.
     *
     * @param index the index of the entry to return
     * @return the entry at the specified position in the list
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    T get(int index);

    /**
     * Removes the entry at the specified position in the list.
     * Shifts any subsequent entries to the left (subtracts one from their indices).
     *
     * @param index the index of the entry to remove
     * @return the entry that was removed from the list
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    T remove(int index);

    /**
     * Removes the first occurrence of the specified entry from the list,
     * if it is present. If the list does not contain the entry, it is unchanged.
     *
     * @param newEntry the entry to remove
     * @return true if the entry was removed successfully, false otherwise
     */
    boolean remove(T newEntry);

    /**
     * Replaces the entry at the specified position in the list with the
     * specified entry.
     *
     * @param index the index of the entry to replace
     * @param newEntry the new entry to be stored at the specified position
     * @return the entry previously at the specified position
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    T set(int index, T newEntry);

    /**
     * Checks whether the list contains the specified entry.
     * 
     * @param o the entry to search for
     * @return true if the list contains the entry, false otherwise
     */
    boolean contains(Object o);

    /**
     * Returns the number of entries in the list.
     *
     * @return the number of entries in the list
     */
    int size();

    /**
     * Returns true if the list is empty, false otherwise.
     *
     * @return true if the list is empty, false otherwise
     */
    boolean isEmpty();
}
