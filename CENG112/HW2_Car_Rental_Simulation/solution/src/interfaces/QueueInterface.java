package interfaces;

/**
 * An interface for the ADT Queue.
 */
public interface QueueInterface<T>
{
    /**
     * Adds a new entry to the back of the queue.
     *
     * @param newEntry is the new entry to add to the queue
     */
    void enqueue(T newEntry);
    
    /**
     * Removes and returns the entry at the front of the queue.
     *
     * @return the queue’s front entry
     * @throws NoSuchElementException if the queue is empty
     */
    T dequeue();
    
    /**
     * Retrieves the queue’s front entry without changing the queue in any way.
     *
     * @return the queue’s front entry
     * @throws NoSuchElementException if this queue is empty
     */
    T peek();
    
    /**
     * Detects whether the queue is empty.
     *
     * @return true if this queue contains no elements, false otherwise
     */
    boolean isEmpty();
    
    /**
     * Removes all entries from the queue.
     */
    void clear();

    /**
     * Returns the number of elements in this queue.
     *
     * @return the number of elements in this queue
     */
    int size();
}
