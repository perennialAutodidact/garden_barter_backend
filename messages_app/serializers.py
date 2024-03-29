from rest_framework import serializers
from .models import Inbox, Message, Conversation
from users_app.serializers import UserMessageSerializer

class MessageSerializer(serializers.ModelSerializer):
    sender = UserMessageSerializer(read_only=True)
    recipient = UserMessageSerializer(read_only=True)
    
    class Meta:
        model = Message
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)
    sender = UserMessageSerializer()
    recipient = UserMessageSerializer()

    class Meta:
        model = Conversation
        fields = ['uuid', 'messages', 'sender', 'recipient']

class InboxSerializer(serializers.ModelSerializer):
    conversations = ConversationSerializer(many=True)
    user = UserMessageSerializer()
    class Meta:
        model = Inbox
        fields = '__all__'
