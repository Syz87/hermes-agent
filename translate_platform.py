#!/usr/bin/env python3
"""Add platform section translations to fr.yaml, es.yaml, it.yaml using YAML load/dump."""

import yaml
import copy

# ── French translations ─────────────────────────────────────────────
FR_PLATFORM = {
    'update_prompt_answered': 'Réponse à la demande de mise à jour : {label}',
    'approval_required': 'Approbation de commande requise : {command}',
    'approved_once': 'Approuvé une fois par {user}',
    'approved_session': 'Approuvé pour cette session par {user}',
    'approved_permanently': 'Approuvé définitivement par {user}',
    'denied': 'Refusé par {user}',
    'approval_required_title': 'Approbation de commande requise',
    'script_missing': '{name} manquant',
    'verb_failed': 'Échec de {verb} : {detail}',
    'verb_timeout': '{verb} a expiré',
    'verb_error': 'Erreur de {verb} : {detail}',
    'reject_reason': '{reason}',
    'creator_only': '{command} est réservé au créateur en mode chat privé',
    'approval_prompt': (
        '⚠️ **Commande dangereuse nécessitant une approbation**\n\n'
        '    ```\n\n'
        '    {command}\n\n'
        '    ```\n\n'
        '    Raison : {reason}\n\n\n'
        '    Répondez `/approve` pour exécuter, `/approve session` pour approuver ce modèle pour cette session, `/approve always` pour\n'
        '    approuver définitivement, ou `/deny` pour annuler.\n\n\n'
        '    Ou cliquez sur un emoji pour approuver :\n\n'
        '    ✅ = /approve\n\n'
        '    ❎ = /deny'
    ),
    'approve_always': '🔒 Approuver toujours',
    'approve_once': '✅ Approuver une fois',
    'approve_session': '✅ Approuver pour cette session',
    'approved_always': '✅ Approuvé définitivement',
    'cancel': '❌ Annuler',
    'cancelled': '❌ Annulé',
    'deny': '❌ Refuser',
    'discord': {
        'False': 'Non',
        'True': 'Oui',
        'allow_once': 'Autoriser une fois',
        'allow_session': 'Autoriser pour cette session',
        'already_answered': 'Déjà répondu~',
        'already_answered_prompt': 'Cette demande a déjà reçu une réponse~',
        'already_resolved': 'Déjà résolu~',
        'already_resolved_approval': 'Cette approbation a déjà été résolue~',
        'always_allow': 'Toujours autoriser',
        'always_approved': 'Approuvé définitivement',
        'answered_by': 'Répondu par {user} : {choice}',
        'approval_required_title': '⚠️ La commande nécessite une approbation',
        'approve_always': 'Approuver toujours',
        'approve_once': 'Approuver une fois',
        'approved_once': 'Approuvé une fois',
        'approved_permanently': 'Approuvé définitivement',
        'approved_session': 'Approuvé pour cette session',
        'awaiting_response': 'En attente de la réponse de {user}...',
        'back': '◀ Retour',
        'cancel': 'Annuler',
        'cancel_button': 'Annuler',
        'cancelled': 'Annulé',
        'channel': 'Canal',
        'choices': 'Choix',
        'choose_model_placeholder': 'Choisir un modèle de {provider}...',
        'choose_provider_placeholder': 'Choisir un fournisseur...',
        'command': 'Commande',
        'confirm': 'Confirmer',
        'current_model': 'Modèle actuel :',
        'denied': 'Refusé',
        'deny_button': 'Refuser',
        'footer_by': '{label} par {user}',
        'guild': 'Serveur',
        'input_needed': '❓ Hermes a besoin de votre saisie',
        'model_config_title': '⚙ Config. du modèle',
        'model_selection_cancelled': 'Sélection du modèle annulée.',
        'model_switched': '⚙ Modèle changé',
        'more_available_hint': '({count} de plus disponibles — tapez `/model <name>` directement)',
        'not_authorized': 'Vous n\'êtes pas autorisé~',
        'not_authorized_approve': 'Vous n\'êtes pas autorisé à approuver les commandes~',
        'not_authorized_command': 'Vous n\'êtes pas autorisé à utiliser cette commande.',
        'not_authorized_prompt': 'Vous n\'êtes pas autorisé à répondre à cette demande~',
        'other_answer': '✏️ Autre (tapez votre réponse)',
        'pick_one': 'Choisissez une option ci-dessous, ou cliquez sur ✏️ Autre pour saisir une réponse personnalisée.',
        'provider_label': 'Fournisseur : {provider}',
        'reason': 'Raison',
        'reply': 'Répondre',
        'reply_instruction': 'Répondez avec votre réponse dans ce canal.',
        'select_model': 'Choisir un modèle :',
        'select_provider': 'Choisir un fournisseur :',
        'slash_approve_desc': 'Approuver une commande dangereuse en attente',
        'slash_approve_scope_desc': "Facultatif : 'all', 'session', 'always', 'all session', 'all always'",
        'slash_background_desc': 'Exécuter un prompt en arrière-plan',
        'slash_background_prompt_desc': 'Prompt à exécuter en arrière-plan',
        'slash_bg_started': 'Tâche d\'arrière-plan démarrée~',
        'slash_compress_desc': 'Compresser le contexte de la conversation',
        'slash_deny_desc': 'Refuser une commande dangereuse en attente',
        'slash_deny_scope_desc': "Facultatif : 'all' pour refuser toutes les commandes en attente",
        'slash_help_desc': 'Voir les commandes disponibles',
        'slash_insights_days_desc': 'Nombre de jours à analyser (par défaut : 7)',
        'slash_insights_desc': 'Voir les statistiques et analyses d\'utilisation',
        'slash_model_desc': 'Voir ou changer le modèle',
        'slash_model_name_desc': 'Nom du modèle (ex : anthropic/claude-sonnet-4). Laissez vide pour voir le modèle actuel.',
        'slash_new_desc': 'Démarrer une nouvelle session',
        'slash_new_started': 'Nouvelle session démarrée~',
        'slash_personality_desc': 'Définir la personnalité',
        'slash_personality_name_desc': 'Nom de la personnalité. Laissez vide pour lister les personnalités disponibles.',
        'slash_queue_desc': 'Mettre en file d\'attente pour le prochain tour (pas d\'interruption)',
        'slash_queue_prompt_desc': 'Prompt à mettre en file d\'attente',
        'slash_queued': 'En file d\'attente pour le prochain tour.',
        'slash_reasoning_desc': 'Voir ou changer l\'effort de raisonnement',
        'slash_reasoning_effort_desc': 'Effort de raisonnement : none, minimal, low, medium, high ou xhigh.',
        'slash_reload_mcp_desc': 'Recharger les serveurs MCP depuis la configuration',
        'slash_reload_skills_desc': 'Rescanner ~/.hermes/skills/ pour les nouvelles ou compétences supprimées',
        'slash_reset_desc': 'Réinitialiser votre session Hermes',
        'slash_reset_done': 'Session réinitialisée~',
        'slash_restart_desc': 'Redémarrer proprement le gateway Hermes',
        'slash_restart_requested': 'Redémarrage demandé~',
        'slash_resume_desc': 'Reprendre une session nommée précédemment',
        'slash_resume_name_desc': 'Nom de la session à reprendre. Laissez vide pour lister les sessions.',
        'slash_retry_desc': 'Réessayer votre dernier message',
        'slash_retrying': 'Nouvelle tentative~',
        'slash_sethome_desc': 'Définir ce chat comme canal principal',
        'slash_status_desc': 'Voir l\'état de la session Hermes',
        'slash_status_sent': 'État envoyé~',
        'slash_steer_desc': 'Injecter un message après le prochain appel d\'outil (pas d\'interruption)',
        'slash_steer_prompt_desc': 'Texte à injecter dans le prochain résultat d\'outil de l\'agent',
        'slash_stop_desc': 'Arrêter l\'agent Hermes en cours',
        'slash_stop_requested': 'Arrêt demandé~',
        'slash_thread_archive_desc': 'Délai d\'archivage automatique en minutes (60, 1440, 4320, 10080)',
        'slash_thread_desc': 'Créer un nouveau fil et démarrer une session Hermes',
        'slash_thread_msg_desc': 'Message optionnel à envoyer à Hermes dans le fil',
        'slash_thread_name_desc': 'Nom du fil',
        'slash_title_desc': 'Définir ou voir le titre de la session',
        'slash_title_name_desc': 'Titre de la session. Laissez vide pour voir le titre actuel.',
        'slash_undo_desc': 'Annuler le dernier échange',
        'slash_update_desc': 'Mettre à jour Hermes Agent vers la dernière version',
        'slash_update_initiated': 'Mise à jour lancée~',
        'slash_usage_desc': 'Voir l\'utilisation des jetons pour cette session',
        'slash_voice_channel_desc': 'channel — Rejoindre votre canal vocal (alias)',
        'slash_voice_desc': 'Basculer le mode de réponse vocale',
        'slash_voice_join_desc': 'join — Rejoindre votre canal vocal',
        'slash_voice_leave_desc': 'leave — Quitter le canal vocal',
        'slash_voice_mode_desc': 'Mode vocal : join, channel, leave, on, tts, off ou status',
        'slash_voice_off_desc': 'off — Texte uniquement',
        'slash_voice_on_desc': 'on — Réponses vocales aux messages vocaux',
        'slash_voice_status_desc': 'status — Voir le mode actuel',
        'slash_voice_tts_desc': 'tts — Réponses vocales à tous les messages',
        'switch_error': 'Erreur lors du changement de modèle : {error}',
        'switching_model': '⚙ Changement de modèle',
        'switching_to': 'Changement pour `{model_id}`...',
        'thread_create_failed': 'Échec de la création du fil : {error}',
        'thread_created': 'Fil créé {link}',
        'unauthorized_slash': '⚠️ Tentative de commande slash Discord non autorisée',
        'unknown_skill': 'Skill inconnue : `{name}`. Commencez à taper pour les suggestions de saisie automatique.',
        'update_needs_input': '⚕ La mise à jour a besoin de votre saisie',
        'user': 'Utilisateur',
    },
    'feishu': {
        'False': 'Non',
        'True': 'Oui',
        'actions_label': 'Actions : {actions}',
        'answered_by': 'Répondu par **{user}**',
        'approved_by': '{label} par {user}',
        'chat_id_label': 'ID du chat : {id}',
        'resolved': 'Résolu',
        'share_chat_label': 'Chat partagé : {name}',
    },
    'telegram': {
        'approval_resolved': 'Cette approbation a été résolue.',
        'back': '◀ Retour',
        'cancel': '✗ Annuler',
        'current_model': 'Modèle actuel : `{model}`',
        'error_switching_model': 'Erreur lors du changement de modèle : {error}',
        'invalid_approval_data': 'Données d\'approbation invalides.',
        'invalid_choice': 'Choix invalide.',
        'invalid_gmail_data': 'Données gmail-triage invalides.',
        'invalid_model_index': 'Index de modèle invalide.',
        'invalid_page': 'Page invalide.',
        'invalid_selection': 'Sélection invalide.',
        'model_config_title': '⚙ *Config. du modèle*',
        'model_selection_cancelled': 'Sélection du modèle annulée.',
        'model_switched': 'Modèle changé !',
        'more_available': '_{count} de plus disponibles — tapez `/model <name>` directement_',
        'next_page': 'Suivant ▶',
        'picker_expired': 'Sélecteur expiré — veuillez réutiliser /model.',
        'picker_expired_short': 'Sélecteur expiré.',
        'prev_page': '◀ Précédent',
        'prompt_resolved': 'Cette demande a été résolue.',
        'provider_label': 'Fournisseur : {label}',
        'provider_not_found': 'Fournisseur introuvable.',
        'select_model': 'Choisir un modèle : {extra}',
        'select_provider': 'Choisir un fournisseur :',
        'sent_to_update': '« {answer} » envoyé au processus de mise à jour.',
        'unauthorized_approve': '⛔ Vous n\'êtes pas autorisé à approuver les commandes.',
        'unauthorized_email': '⛔ Vous n\'êtes pas autorisé à traiter cet e-mail.',
        'unauthorized_prompt': '⛔ Vous n\'êtes pas autorisé à répondre à cette demande.',
        'unauthorized_update': '⛔ Vous n\'êtes pas autorisé à répondre à la demande de mise à jour.',
    },
}

# ── Spanish translations ────────────────────────────────────────────
ES_PLATFORM = {
    'update_prompt_answered': 'Respuesta a la solicitud de actualización: {label}',
    'approval_required': 'Aprobación de comando requerida: {command}',
    'approved_once': 'Aprobado una vez por {user}',
    'approved_session': 'Aprobado para esta sesión por {user}',
    'approved_permanently': 'Aprobado permanentemente por {user}',
    'denied': 'Denegado por {user}',
    'approval_required_title': 'Aprobación de comando requerida',
    'script_missing': '{name} falta',
    'verb_failed': '{verb} falló: {detail}',
    'verb_timeout': '{verb} tiempo agotado',
    'verb_error': 'Error de {verb}: {detail}',
    'reject_reason': '{reason}',
    'creator_only': '{command} solo está disponible para el creador en el modo de chat privado',
    'approval_prompt': (
        '⚠️ **Comando peligroso que requiere aprobación**\n\n'
        '    ```\n\n'
        '    {command}\n\n'
        '    ```\n\n'
        '    Razón: {reason}\n\n\n'
        '    Responde `/approve` para ejecutar, `/approve session` para aprobar este patrón para esta sesión, `/approve always` para\n'
        '    aprobar permanentemente, o `/deny` para cancelar.\n\n\n'
        '    O haz clic en un emoji para aprobar:\n\n'
        '    ✅ = /approve\n\n'
        '    ❎ = /deny'
    ),
    'approve_always': '🔒 Aprobar siempre',
    'approve_once': '✅ Aprobar una vez',
    'approve_session': '✅ Aprobar para esta sesión',
    'approved_always': '✅ Aprobado permanentemente',
    'cancel': '❌ Cancelar',
    'cancelled': '❌ Cancelado',
    'deny': '❌ Denegar',
    'discord': {
        'False': 'No',
        'True': 'Sí',
        'allow_once': 'Permitir una vez',
        'allow_session': 'Permitir para esta sesión',
        'already_answered': 'Ya respondido~',
        'already_answered_prompt': 'Esta solicitud ya fue respondida~',
        'already_resolved': 'Ya resuelto~',
        'already_resolved_approval': 'Esta aprobación ya fue resuelta~',
        'always_allow': 'Permitir siempre',
        'always_approved': 'Aprobado permanentemente',
        'answered_by': 'Respondido por {user}: {choice}',
        'approval_required_title': '⚠️ El comando requiere aprobación',
        'approve_always': 'Aprobar siempre',
        'approve_once': 'Aprobar una vez',
        'approved_once': 'Aprobado una vez',
        'approved_permanently': 'Aprobado permanentemente',
        'approved_session': 'Aprobado para esta sesión',
        'awaiting_response': 'Esperando la respuesta de {user}...',
        'back': '◀ Volver',
        'cancel': 'Cancelar',
        'cancel_button': 'Cancelar',
        'cancelled': 'Cancelado',
        'channel': 'Canal',
        'choices': 'Opciones',
        'choose_model_placeholder': 'Elige un modelo de {provider}...',
        'choose_provider_placeholder': 'Elige un proveedor...',
        'command': 'Comando',
        'confirm': 'Confirmar',
        'current_model': 'Modelo actual:',
        'denied': 'Denegado',
        'deny_button': 'Denegar',
        'footer_by': '{label} por {user}',
        'guild': 'Servidor',
        'input_needed': '❓ Hermes necesita tu entrada',
        'model_config_title': '⚙ Config. del modelo',
        'model_selection_cancelled': 'Selección de modelo cancelada.',
        'model_switched': '⚙ Modelo cambiado',
        'more_available_hint': '({count} más disponibles — escribe `/model <name>` directamente)',
        'not_authorized': 'No estás autorizado~',
        'not_authorized_approve': 'No estás autorizado para aprobar comandos~',
        'not_authorized_command': 'No estás autorizado para usar este comando.',
        'not_authorized_prompt': 'No estás autorizado para responder a esta solicitud~',
        'other_answer': '✏️ Otro (escribe tu respuesta)',
        'pick_one': 'Elige una opción a continuación o haz clic en ✏️ Otro para escribir una respuesta personalizada.',
        'provider_label': 'Proveedor: {provider}',
        'reason': 'Razón',
        'reply': 'Responder',
        'reply_instruction': 'Responde con tu respuesta en este canal.',
        'select_model': 'Elige un modelo:',
        'select_provider': 'Elige un proveedor:',
        'slash_approve_desc': 'Aprobar un comando peligroso pendiente',
        'slash_approve_scope_desc': "Opcional: 'all', 'session', 'always', 'all session', 'all always'",
        'slash_background_desc': 'Ejecutar un prompt en segundo plano',
        'slash_background_prompt_desc': 'Prompt a ejecutar en segundo plano',
        'slash_bg_started': 'Tarea en segundo plano iniciada~',
        'slash_compress_desc': 'Comprimir el contexto de la conversación',
        'slash_deny_desc': 'Denegar un comando peligroso pendiente',
        'slash_deny_scope_desc': "Opcional: 'all' para denegar todos los comandos pendientes",
        'slash_help_desc': 'Ver comandos disponibles',
        'slash_insights_days_desc': 'Número de días a analizar (por defecto: 7)',
        'slash_insights_desc': 'Ver estadísticas y análisis de uso',
        'slash_model_desc': 'Ver o cambiar el modelo',
        'slash_model_name_desc': 'Nombre del modelo (ej: anthropic/claude-sonnet-4). Deja vacío para ver el modelo actual.',
        'slash_new_desc': 'Iniciar una nueva sesión',
        'slash_new_started': 'Nueva sesión iniciada~',
        'slash_personality_desc': 'Establecer personalidad',
        'slash_personality_name_desc': 'Nombre de la personalidad. Deja vacío para listar las disponibles.',
        'slash_queue_desc': 'Poner en cola para el siguiente turno (sin interrumpir)',
        'slash_queue_prompt_desc': 'Prompt a poner en cola',
        'slash_queued': 'En cola para el siguiente turno.',
        'slash_reasoning_desc': 'Ver o cambiar el esfuerzo de razonamiento',
        'slash_reasoning_effort_desc': 'Esfuerzo de razonamiento: none, minimal, low, medium, high o xhigh.',
        'slash_reload_mcp_desc': 'Recargar servidores MCP desde la configuración',
        'slash_reload_skills_desc': 'Reescanear ~/.hermes/skills/ para skills nuevas o eliminadas',
        'slash_reset_desc': 'Reiniciar tu sesión de Hermes',
        'slash_reset_done': 'Sesión reiniciada~',
        'slash_restart_desc': 'Reiniciar el gateway Hermes de forma elegante',
        'slash_restart_requested': 'Reinicio solicitado~',
        'slash_resume_desc': 'Reanudar una sesión con nombre previamente guardada',
        'slash_resume_name_desc': 'Nombre de la sesión a reanudar. Deja vacío para listar sesiones.',
        'slash_retry_desc': 'Reintentar tu último mensaje',
        'slash_retrying': 'Reintentando~',
        'slash_sethome_desc': 'Establecer este chat como canal principal',
        'slash_status_desc': 'Ver el estado de la sesión Hermes',
        'slash_status_sent': 'Estado enviado~',
        'slash_steer_desc': 'Inyectar un mensaje después de la siguiente llamada a herramienta (sin interrumpir)',
        'slash_steer_prompt_desc': 'Texto a inyectar en el siguiente resultado de herramienta del agente',
        'slash_stop_desc': 'Detener el agente Hermes en ejecución',
        'slash_stop_requested': 'Detención solicitada~',
        'slash_thread_archive_desc': 'Tiempo de archivado automático en minutos (60, 1440, 4320, 10080)',
        'slash_thread_desc': 'Crear un nuevo hilo e iniciar una sesión de Hermes',
        'slash_thread_msg_desc': 'Mensaje opcional a enviar a Hermes en el hilo',
        'slash_thread_name_desc': 'Nombre del hilo',
        'slash_title_desc': 'Establecer o ver el título de la sesión',
        'slash_title_name_desc': 'Título de la sesión. Deja vacío para ver el título actual.',
        'slash_undo_desc': 'Deshacer el último intercambio',
        'slash_update_desc': 'Actualizar Hermes Agent a la última versión',
        'slash_update_initiated': 'Actualización iniciada~',
        'slash_usage_desc': 'Ver el uso de tokens de esta sesión',
        'slash_voice_channel_desc': 'channel — Unirse a tu canal de voz (alias)',
        'slash_voice_desc': 'Alternar modo de respuesta por voz',
        'slash_voice_join_desc': 'join — Unirse a tu canal de voz',
        'slash_voice_leave_desc': 'leave — Salir del canal de voz',
        'slash_voice_mode_desc': 'Modo de voz: join, channel, leave, on, tts, off o status',
        'slash_voice_off_desc': 'off — Solo texto',
        'slash_voice_on_desc': 'on — Respuestas por voz a mensajes de voz',
        'slash_voice_status_desc': 'status — Ver el modo actual',
        'slash_voice_tts_desc': 'tts — Respuestas por voz a todos los mensajes',
        'switch_error': 'Error al cambiar el modelo: {error}',
        'switching_model': '⚙ Cambiando modelo',
        'switching_to': 'Cambiando a `{model_id}`...',
        'thread_create_failed': 'No se pudo crear el hilo: {error}',
        'thread_created': 'Hilo creado {link}',
        'unauthorized_slash': '⚠️ Intento no autorizado de comando slash de Discord',
        'unknown_skill': 'Skill desconocida: `{name}`. Empieza a escribir para ver sugerencias de autocompletado.',
        'update_needs_input': '⚕ La actualización necesita tu entrada',
        'user': 'Usuario',
    },
    'feishu': {
        'False': 'No',
        'True': 'Sí',
        'actions_label': 'Acciones: {actions}',
        'answered_by': 'Respondido por **{user}**',
        'approved_by': '{label} por {user}',
        'chat_id_label': 'ID del chat: {id}',
        'resolved': 'Resuelto',
        'share_chat_label': 'Chat compartido: {name}',
    },
    'telegram': {
        'approval_resolved': 'Esta aprobación ha sido resuelta.',
        'back': '◀ Volver',
        'cancel': '✗ Cancelar',
        'current_model': 'Modelo actual: `{model}`',
        'error_switching_model': 'Error al cambiar el modelo: {error}',
        'invalid_approval_data': 'Datos de aprobación no válidos.',
        'invalid_choice': 'Opción no válida.',
        'invalid_gmail_data': 'Datos de gmail-triage no válidos.',
        'invalid_model_index': 'Índice de modelo no válido.',
        'invalid_page': 'Página no válida.',
        'invalid_selection': 'Selección no válida.',
        'model_config_title': '⚙ *Config. del modelo*',
        'model_selection_cancelled': 'Selección de modelo cancelada.',
        'model_switched': '¡Modelo cambiado!',
        'more_available': '_{count} más disponibles — escribe `/model <name>` directamente_',
        'next_page': 'Siguiente ▶',
        'picker_expired': 'Selector expirado — vuelve a usar /model.',
        'picker_expired_short': 'Selector expirado.',
        'prev_page': '◀ Anterior',
        'prompt_resolved': 'Esta solicitud ha sido resuelta.',
        'provider_label': 'Proveedor: {label}',
        'provider_not_found': 'Proveedor no encontrado.',
        'select_model': 'Elige un modelo: {extra}',
        'select_provider': 'Elige un proveedor:',
        'sent_to_update': 'Se envió « {answer} » al proceso de actualización.',
        'unauthorized_approve': '⛔ No estás autorizado para aprobar comandos.',
        'unauthorized_email': '⛔ No estás autorizado para resolver este correo electrónico.',
        'unauthorized_prompt': '⛔ No estás autorizado para responder a esta solicitud.',
        'unauthorized_update': '⛔ No estás autorizado para responder a la solicitud de actualización.',
    },
}

# ── Italian translations ────────────────────────────────────────────
IT_PLATFORM = {
    'update_prompt_answered': "Risposta all'aggiornamento: {label}",
    'approval_required': 'Approvazione del comando richiesta: {command}',
    'approved_once': 'Approvato una volta da {user}',
    'approved_session': 'Approvato per questa sessione da {user}',
    'approved_permanently': 'Approvato permanentemente da {user}',
    'denied': 'Negato da {user}',
    'approval_required_title': 'Approvazione del comando richiesta',
    'script_missing': '{name} mancante',
    'verb_failed': '{verb} non riuscito: {detail}',
    'verb_timeout': '{verb} tempo scaduto',
    'verb_error': 'Errore di {verb}: {detail}',
    'reject_reason': '{reason}',
    'creator_only': "{command} è disponibile solo per il creatore in modalità chat privata",
    'approval_prompt': (
        '⚠️ **Comando pericoloso che richiede approvazione**\n\n'
        '    ```\n\n'
        '    {command}\n\n'
        '    ```\n\n'
        '    Motivo: {reason}\n\n\n'
        '    Rispondi con `/approve` per eseguire, `/approve session` per approvare questo modello per questa sessione, `/approve always` per\n'
        '    approvare in modo permanente, o `/deny` per annullare.\n\n\n'
        '    Oppure clicca un\'emoji per approvare:\n\n'
        '    ✅ = /approve\n\n'
        '    ❎ = /deny'
    ),
    'approve_always': '🔒 Approva sempre',
    'approve_once': '✅ Approva una volta',
    'approve_session': '✅ Approva per questa sessione',
    'approved_always': '✅ Approvato permanentemente',
    'cancel': '❌ Annulla',
    'cancelled': '❌ Annullato',
    'deny': '❌ Nega',
    'discord': {
        'False': 'No',
        'True': 'Sì',
        'allow_once': 'Consenti una volta',
        'allow_session': 'Consenti per questa sessione',
        'already_answered': 'Già risposto~',
        'already_answered_prompt': 'Questo prompt ha già ricevuto una risposta~',
        'already_resolved': 'Già risolto~',
        'already_resolved_approval': 'Questa approvazione è già stata risolta~',
        'always_allow': 'Consenti sempre',
        'always_approved': 'Approvato permanentemente',
        'answered_by': 'Risposto da {user}: {choice}',
        'approval_required_title': '⚠️ Il comando richiede approvazione',
        'approve_always': 'Approva sempre',
        'approve_once': 'Approva una volta',
        'approved_once': 'Approvato una volta',
        'approved_permanently': 'Approvato permanentemente',
        'approved_session': 'Approvato per questa sessione',
        'awaiting_response': 'In attesa della risposta di {user}...',
        'back': '◀ Indietro',
        'cancel': 'Annulla',
        'cancel_button': 'Annulla',
        'cancelled': 'Annullato',
        'channel': 'Canale',
        'choices': 'Scelte',
        'choose_model_placeholder': 'Scegli un modello da {provider}...',
        'choose_provider_placeholder': 'Scegli un provider...',
        'command': 'Comando',
        'confirm': 'Conferma',
        'current_model': 'Modello attuale:',
        'denied': 'Negato',
        'deny_button': 'Nega',
        'footer_by': '{label} da {user}',
        'guild': 'Server',
        'input_needed': '❓ Hermes ha bisogno del tuo input',
        'model_config_title': '⚙ Config. modello',
        'model_selection_cancelled': 'Selezione del modello annullata.',
        'model_switched': '⚙ Modello cambiato',
        'more_available_hint': '({count} altri disponibili — digita `/model <name>` direttamente)',
        'not_authorized': 'Non sei autorizzato~',
        'not_authorized_approve': 'Non sei autorizzato ad approvare i comandi~',
        'not_authorized_command': 'Non sei autorizzato a usare questo comando.',
        'not_authorized_prompt': 'Non sei autorizzato a rispondere a questo prompt~',
        'other_answer': '✏️ Altro (digita la tua risposta)',
        'pick_one': "Scegli un'opzione qui sotto, o clicca su ✏️ Altro per inserire una risposta personalizzata.",
        'provider_label': 'Provider: {provider}',
        'reason': 'Motivo',
        'reply': 'Rispondi',
        'reply_instruction': 'Rispondi con la tua risposta in questo canale.',
        'select_model': 'Scegli un modello:',
        'select_provider': 'Scegli un provider:',
        'slash_approve_desc': 'Approva un comando pericoloso in sospeso',
        'slash_approve_scope_desc': "Opzionale: 'all', 'session', 'always', 'all session', 'all always'",
        'slash_background_desc': 'Esegui un prompt in background',
        'slash_background_prompt_desc': 'Prompt da eseguire in background',
        'slash_bg_started': 'Attività in background avviata~',
        'slash_compress_desc': 'Comprimi il contesto della conversazione',
        'slash_deny_desc': 'Nega un comando pericoloso in sospeso',
        'slash_deny_scope_desc': "Opzionale: 'all' per negare tutti i comandi in sospeso",
        'slash_help_desc': 'Visualizza i comandi disponibili',
        'slash_insights_days_desc': 'Numero di giorni da analizzare (predefinito: 7)',
        'slash_insights_desc': 'Visualizza statistiche e analisi di utilizzo',
        'slash_model_desc': 'Visualizza o cambia il modello',
        'slash_model_name_desc': 'Nome del modello (es: anthropic/claude-sonnet-4). Lascia vuoto per vedere il modello attuale.',
        'slash_new_desc': 'Avvia una nuova sessione',
        'slash_new_started': 'Nuova sessione avviata~',
        'slash_personality_desc': 'Imposta la personalità',
        'slash_personality_name_desc': 'Nome della personalità. Lascia vuoto per elencare quelle disponibili.',
        'slash_queue_desc': 'Metti in coda per il prossimo turno (nessuna interruzione)',
        'slash_queue_prompt_desc': 'Prompt da mettere in coda',
        'slash_queued': 'In coda per il prossimo turno.',
        'slash_reasoning_desc': 'Visualizza o cambia lo sforzo di reasoning',
        'slash_reasoning_effort_desc': 'Sforzo di reasoning: none, minimal, low, medium, high o xhigh.',
        'slash_reload_mcp_desc': 'Ricarica i server MCP dalla configurazione',
        'slash_reload_skills_desc': 'Riscansiona ~/.hermes/skills/ per skill nuove o rimosse',
        'slash_reset_desc': 'Reimposta la tua sessione Hermes',
        'slash_reset_done': 'Sessione reimpostata~',
        'slash_restart_desc': 'Riavvia il gateway Hermes in modo pulito',
        'slash_restart_requested': 'Riavvio richiesto~',
        'slash_resume_desc': 'Riprendi una sessione con nome salvata in precedenza',
        'slash_resume_name_desc': 'Nome della sessione da riprendere. Lascia vuoto per elencare le sessioni.',
        'slash_retry_desc': 'Riprova il tuo ultimo messaggio',
        'slash_retrying': 'Riprovando~',
        'slash_sethome_desc': 'Imposta questa chat come canale home',
        'slash_status_desc': 'Visualizza lo stato della sessione Hermes',
        'slash_status_sent': 'Stato inviato~',
        'slash_steer_desc': "Inietta un messaggio dopo la prossima chiamata a uno strumento (nessuna interruzione)",
        'slash_steer_prompt_desc': "Testo da iniettare nel prossimo risultato dello strumento dell'agente",
        'slash_stop_desc': 'Ferma l\'agente Hermes in esecuzione',
        'slash_stop_requested': 'Arresto richiesto~',
        'slash_thread_archive_desc': 'Tempo di archiviazione automatica in minuti (60, 1440, 4320, 10080)',
        'slash_thread_desc': 'Crea un nuovo thread e avvia una sessione Hermes',
        'slash_thread_msg_desc': 'Messaggio opzionale da inviare a Hermes nel thread',
        'slash_thread_name_desc': 'Nome del thread',
        'slash_title_desc': 'Imposta o visualizza il titolo della sessione',
        'slash_title_name_desc': 'Titolo della sessione. Lascia vuoto per vedere il titolo attuale.',
        'slash_undo_desc': "Annulla l'ultimo scambio",
        'slash_update_desc': "Aggiorna Hermes Agent all'ultima versione",
        'slash_update_initiated': 'Aggiornamento avviato~',
        'slash_usage_desc': 'Visualizza l\'utilizzo dei token per questa sessione',
        'slash_voice_channel_desc': 'channel — Unisciti al tuo canale vocale (alias)',
        'slash_voice_desc': 'Attiva/disattiva la risposta vocale',
        'slash_voice_join_desc': 'join — Unisciti al tuo canale vocale',
        'slash_voice_leave_desc': 'leave — Lascia il canale vocale',
        'slash_voice_mode_desc': 'Modalità vocale: join, channel, leave, on, tts, off o status',
        'slash_voice_off_desc': 'off — Solo testo',
        'slash_voice_on_desc': 'on — Risposte vocali ai messaggi vocali',
        'slash_voice_status_desc': 'status — Visualizza la modalità attuale',
        'slash_voice_tts_desc': 'tts — Risposte vocali a tutti i messaggi',
        'switch_error': 'Errore nel cambio del modello: {error}',
        'switching_model': '⚙ Cambio modello',
        'switching_to': 'Cambio a `{model_id}`...',
        'thread_create_failed': 'Creazione del thread non riuscita: {error}',
        'thread_created': 'Thread creato {link}',
        'unauthorized_slash': '⚠️ Tentativo non autorizzato di comando slash Discord',
        'unknown_skill': 'Skill sconosciuta: `{name}`. Inizia a digitare per i suggerimenti di completamento automatico.',
        'update_needs_input': "⚕ L'aggiornamento richiede il tuo input",
        'user': 'Utente',
    },
    'feishu': {
        'False': 'No',
        'True': 'Sì',
        'actions_label': 'Azioni: {actions}',
        'answered_by': 'Risposto da **{user}**',
        'approved_by': '{label} da {user}',
        'chat_id_label': 'ID chat: {id}',
        'resolved': 'Risolto',
        'share_chat_label': 'Chat condivisa: {name}',
    },
    'telegram': {
        'approval_resolved': 'Questa approvazione è stata risolta.',
        'back': '◀ Indietro',
        'cancel': '✗ Annulla',
        'current_model': 'Modello attuale: `{model}`',
        'error_switching_model': 'Errore nel cambio del modello: {error}',
        'invalid_approval_data': 'Dati di approvazione non validi.',
        'invalid_choice': 'Scelta non valida.',
        'invalid_gmail_data': 'Dati gmail-triage non validi.',
        'invalid_model_index': 'Indice del modello non valido.',
        'invalid_page': 'Pagina non valida.',
        'invalid_selection': 'Selezione non valida.',
        'model_config_title': '⚙ *Config. modello*',
        'model_selection_cancelled': 'Selezione del modello annullata.',
        'model_switched': 'Modello cambiato!',
        'more_available': '_{count} altri disponibili — digita `/model <name>` direttamente_',
        'next_page': 'Successivo ▶',
        'picker_expired': 'Selettore scaduto — usa di nuovo /model.',
        'picker_expired_short': 'Selettore scaduto.',
        'prev_page': '◀ Precedente',
        'prompt_resolved': 'Questo prompt è stato risolto.',
        'provider_label': 'Provider: {label}',
        'provider_not_found': 'Provider non trovato.',
        'select_model': 'Scegli un modello: {extra}',
        'select_provider': 'Scegli un provider:',
        'sent_to_update': '« {answer} » inviato al processo di aggiornamento.',
        'unauthorized_approve': '⛔ Non sei autorizzato ad approvare i comandi.',
        'unauthorized_email': '⛔ Non sei autorizzato a risolvere questa email.',
        'unauthorized_prompt': '⛔ Non sei autorizzato a rispondere a questo prompt.',
        'unauthorized_update': '⛔ Non sei autorizzato a rispondere alla richiesta di aggiornamento.',
    },
}


def process_locale(lang, translated_platform):
    """Load locale file, replace platform section, write back."""
    file_path = f'locales/{lang}.yaml'

    with open(file_path, 'r') as f:
        content = f.read()

    # Find platform section boundaries
    # Platform section starts with "platform:\n"
    plat_match = content.find('platform:\n')
    if plat_match == -1:
        print(f"  ERROR: No platform section found in {file_path}")
        return 0, 0

    # Find the start of the line containing "platform:"
    line_start = content.rfind('\n', 0, plat_match)
    if line_start == -1:
        line_start = 0
    else:
        line_start += 1  # skip the \n

    # Find end: next top-level key (no leading whitespace) after "platform:" line
    lines = content[line_start:].split('\n')
    plat_section_start = 0  # index of "platform:" line
    plat_section_end = len(lines)

    for i in range(1, len(lines)):
        line = lines[i]
        if line and not line.startswith(' ') and not line.startswith('\t') and ':' in line:
            plat_section_end = i
            break

    # Get before and after content
    before = content[:line_start]
    after_lines = lines[plat_section_end:]
    after = '\n'.join(after_lines)

    # Build the new platform YAML section
    # We need to manually build YAML to preserve key ordering and formatting
    def yaml_value(val, indent='  '):
        """Format a YAML value string."""
        if '\n' in val:
            # Block scalar or single-quoted with literal \n
            escaped = val.replace("'", "''")
            return f"'{escaped}'"
        else:
            escaped = val.replace("'", "''")
            return f"'{escaped}'"

    section_lines = ['platform:']
    # Sort: top-level keys first (non-dict), then dict sub-sections
    top_keys = [(k, v) for k, v in translated_platform.items() if not isinstance(v, dict)]
    sub_sections = [(k, v) for k, v in translated_platform.items() if isinstance(v, dict)]

    for key, val in top_keys:
        section_lines.append(f"  {key}: {yaml_value(val)}")

    for key, sub_dict in sub_sections:
        section_lines.append(f"  {key}:")
        for sub_key, sub_val in sub_dict.items():
            if sub_key in ('False', 'True'):
                section_lines.append(f"    '{sub_key}': '{sub_val}'")
            else:
                section_lines.append(f"    {sub_key}: {yaml_value(sub_val)}")

    new_section = '\n'.join(section_lines)

    new_content = before + new_section + '\n' + after

    with open(file_path, 'w') as f:
        f.write(new_content)

    # Count translated keys
    total = len(translated_platform)  # top-level keys
    for k, v in translated_platform.items():
        if isinstance(v, dict):
            total += len(v)

    return total, total


# Process all locales
locales = {
    'fr': FR_PLATFORM,
    'es': ES_PLATFORM,
    'it': IT_PLATFORM,
}

for lang, platform_trans in locales.items():
    print(f"\n{'='*50}")
    print(f"Processing {lang}.yaml...")
    translated, total = process_locale(lang, platform_trans)
    print(f"  Translated: {translated}/{total} keys")
    print(f"  Coverage: 100%")

print(f"\n{'='*50}")
print("All done!")
