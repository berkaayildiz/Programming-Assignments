package implementations;

import java.util.NoSuchElementException;

import interfaces.QueueInterface;

/**
 * An array-based implementation of the QueueInterface.
 * For this implementation, the queue is circular and has one unused location.
 */
public final class ArrayQueue<T> implements QueueInterface<T>
{
    private T[] queue;
    private int frontIndex;
    private int backIndex;
    private boolean initialized = false;
    private static final int DEFAULT_CAPACITY = 50;
    private static final int MAX_CAPACITY = 10000;

    public ArrayQueue()
    {
        this(DEFAULT_CAPACITY);
    }

    public ArrayQueue(int initialCapacity)
    {
        checkCapacity(initialCapacity);

        // The cast is safe because the new array contains null entries
        @SuppressWarnings("unchecked")
        T[] tempQueue = (T[]) new Object[initialCapacity + 1]; // + 1 to make sure there is an unused location
        queue = tempQueue;

        frontIndex = 0;
        backIndex = initialCapacity;
        initialized = true;
    }

    public void enqueue(T newEntry)
    {
        checkInitialization();
        ensureCapacity();

        backIndex = (backIndex + 1) % queue.length;
        queue[backIndex] = newEntry;
    }

    public T dequeue()
    {
        checkInitialization();
        if (isEmpty())
            throw new NoSuchElementException();
        else {
            T front = queue[frontIndex];
            queue[frontIndex] = null;
            frontIndex = (frontIndex + 1) % queue.length;
            return front;
        }
    } 

    public T peek()
    {
        checkInitialization();
        if (isEmpty())
            throw new NoSuchElementException();
        else
            return queue[frontIndex];
    } 

    public boolean isEmpty()
    {
        return frontIndex == ((backIndex + 1) % queue.length);
    }

    public void clear()
    {
        while (!isEmpty()) {
            dequeue();
        }
    }

    public int size()
    {
        return (backIndex - frontIndex + queue.length + 1) % queue.length;
    }

    private void ensureCapacity()
    {
        if (frontIndex == ((backIndex + 2) % queue.length)) {
            T[] oldQueue = queue;
            int oldSize = oldQueue.length;
            int newSize = 2 * oldSize;

            checkCapacity(newSize - 1);

            // The cast is safe because the new array contains null entries
            @SuppressWarnings("unchecked")
            T[] tempQueue = (T[]) new Object[newSize];
            queue = tempQueue;
            for (int index = 0; index < oldSize - 1; index++)
            {
                queue[index] = oldQueue[frontIndex];
                frontIndex = (frontIndex + 1) % oldSize;
            }
            frontIndex = 0;
            backIndex = oldSize - 2;
        }
    } 
    
    private void checkInitialization() throws SecurityException
    {
        if (!initialized)
        {
            throw new SecurityException("ArrayQueue object is not initialized properly.");
        }
    }

    private void checkCapacity(int capacity) throws IllegalStateException
    {
        if (capacity > MAX_CAPACITY)
        {
            throw new IllegalStateException("Attempt to create a queue whose capacity exceeds allowed maximum.");
        }
    }
}
