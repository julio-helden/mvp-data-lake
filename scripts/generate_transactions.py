"""
Feature: Generate Transactions

This script generates random transactions and sends them to Kafka.
It limits the number of transactions to avoid infinite loops.
"""

import json
import random
import time
from kafka import KafkaProducer

def generate_transaction():
    """
    Generate a random transaction record.

    Returns:
        dict: A dictionary containing transaction details.
    """
    return {
        "transaction_id": random.randint(1000, 9999),
        "user_id": random.randint(1, 100),
        "amount": round(random.uniform(10.0, 1000.0), 2),
        "timestamp": time.time(),
        "is_fraud": random.choice([0, 0, 0, 1])  # 25% chance of fraud
    }

def main():
    """
    Generate a limited number of transactions and send them to Kafka.
    """
    KAFKA_TOPIC = "transactions"
    KAFKA_SERVER = "localhost:9092"
    MAX_TRANSACTIONS = 100  # Set the limit for transactions

    # Configure Kafka Producer
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

    for i in range(MAX_TRANSACTIONS):
        transaction = generate_transaction()
        producer.send(KAFKA_TOPIC, transaction)
        print(f"Sent transaction {i + 1} to Kafka: {transaction}")
        time.sleep(1)  # Pause for 1 second between transactions

    print(f"Finished sending {MAX_TRANSACTIONS} transactions.")

if __name__ == "__main__":
    main()
